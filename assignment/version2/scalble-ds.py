import asyncio
import aiohttp
from aiohttp import web
import time
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('DistributedSystem')

# ---------------------------
# Load Balancer Implementation
# ---------------------------
class LoadBalancer:
    def __init__(self, port=8000):
        self.port = port
        self.servers = []
        self.next_port = 8001
        self.min_servers = 2
        self.max_servers = 5
        self.started = asyncio.Event()

    def add_server(self, port):
        """Add a new server to the pool"""
        self.servers.append({
            "port": port,
            "load": 0,
            "last_heartbeat": time.time(),
            "active": True
        })
        logger.info(f"Added server on port {port}")

    async def start_server(self):
        """Start a new server instance"""
        port = self.next_port
        self.next_port += 1
        server = Server(port, self.port)
        asyncio.create_task(server.run(self.started))
        self.add_server(port)
        return port

    def get_best_server(self):
        """Select server with lowest load"""
        active_servers = [s for s in self.servers if s["active"]]
        if not active_servers:
            return None
        return min(active_servers, key=lambda x: x["load"])

    async def handle_request(self, request):
        """Route incoming requests to best server"""
        try:
            data = await request.json()
            server = self.get_best_server()
            
            if not server:
                return web.Response(status=503, text="No available servers")
            
            server["load"] += 1
            try:
                async with aiohttp.ClientSession() as session:
                    url = f'http://localhost:{server["port"]}/request'
                    async with session.post(url, json=data) as resp:
                        response = await resp.json()
                        return web.json_response(response)
            except Exception as e:
                logger.error(f"Request failed to server {server['port']}: {str(e)}")
                return web.Response(status=500, text=str(e))
            finally:
                server["load"] -= 1
        except json.JSONDecodeError:
            return web.Response(status=400, text="Invalid JSON")

    async def handle_heartbeat(self, request):
        """Process server heartbeats"""
        try:
            data = await request.json()
            port = data["port"]
            
            for server in self.servers:
                if server["port"] == port:
                    server["last_heartbeat"] = time.time()
                    server["active"] = True
                    logger.debug(f"Heartbeat from server {port}")
                    break
            return web.Response(text="ACK")
        except (json.JSONDecodeError, KeyError):
            return web.Response(status=400, text="Invalid heartbeat")

    async def handle_status(self, request):
        """Return system status"""
        status = {
            "servers": [
                {
                    "port": s["port"],
                    "load": s["load"],
                    "active": s["active"],
                    "last_heartbeat": time.time() - s["last_heartbeat"]
                } 
                for s in self.servers
            ],
            "active_servers": sum(1 for s in self.servers if s["active"]),
            "total_load": sum(s["load"] for s in self.servers),
            "next_port": self.next_port
        }
        return web.json_response(status)

    async def heartbeat_checker(self):
        """Check server heartbeats every 5 seconds"""
        while True:
            await asyncio.sleep(5)
            current_time = time.time()
            
            for server in self.servers:
                if current_time - server["last_heartbeat"] > 10:  # 2 missed heartbeats
                    server["active"] = False
                    logger.warning(f"Server {server['port']} marked as inactive")

    async def auto_scaler(self):
        """Auto-scale servers based on load every 10 seconds"""
        # Wait for initial setup
        await asyncio.sleep(15)
        
        while True:
            await asyncio.sleep(10)
            active_servers = [s for s in self.servers if s["active"]]
            
            if not active_servers:
                continue
                
            total_load = sum(s["load"] for s in active_servers)
            avg_load = total_load / len(active_servers)
            
            # Scale up if needed
            if avg_load > 2 and len(self.servers) < self.max_servers:
                port = await self.start_server()
                logger.info(f"Scaling UP: Started server on port {port}")
            
            # Scale down if needed
            inactive_servers = [s for s in self.servers if not s["active"] and s["load"] == 0]
            if inactive_servers and len(self.servers) > self.min_servers:
                server_to_remove = inactive_servers[0]
                self.servers = [s for s in self.servers if s["port"] != server_to_remove["port"]]
                logger.info(f"Scaling DOWN: Removed server on port {server_to_remove['port']}")

    async def run(self):
        """Run load balancer"""
        app = web.Application()
        app.router.add_post('/request', self.handle_request)
        app.router.add_post('/heartbeat', self.handle_heartbeat)
        app.router.add_get('/status', self.handle_status)
        
        # Start background tasks
        asyncio.create_task(self.heartbeat_checker())
        asyncio.create_task(self.auto_scaler())
        
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, 'localhost', self.port)
        await site.start()
        self.started.set()  # Signal that LB is ready
        logger.info(f"Load Balancer running on port {self.port}")

# ---------------------------
# Server Implementation
# ---------------------------
class Server:
    def __init__(self, port, lb_port):
        self.port = port
        self.lb_port = lb_port
        self.data = {}
        self.replica_ports = []

    async def handle_request(self, request):
        """Handle incoming requests"""
        try:
            data = await request.json()
            response = {}
            
            if data["type"] == "calculate":
                result = sum(data["numbers"])
                response = {"result": result}
                logger.info(f"Server {self.port}: Calculated sum {result}")
                
            elif data["type"] == "store":
                self.data[data["key"]] = data["value"]
                # Replicate to other servers
                await self.replicate_data(data["key"], data["value"])
                response = {"status": "stored"}
                logger.info(f"Server {self.port}: Stored data {data['key']}")
                
            elif data["type"] == "retrieve":
                value = self.data.get(data["key"], "NOT_FOUND")
                response = {"value": value}
                logger.info(f"Server {self.port}: Retrieved {data['key']}")
                
            elif data["type"] == "replicate":
                self.data[data["key"]] = data["value"]
                response = {"status": "replicated"}
                logger.debug(f"Server {self.port}: Replicated {data['key']}")
                
            return web.json_response(response)
        except (json.JSONDecodeError, KeyError) as e:
            logger.error(f"Server {self.port}: Bad request - {str(e)}")
            return web.Response(status=400, text="Invalid request")

    async def replicate_data(self, key, value):
        """Replicate data to all other servers"""
        for port in self.replica_ports:
            if port != self.port:  # Don't replicate to self
                try:
                    async with aiohttp.ClientSession() as session:
                        url = f'http://localhost:{port}/request'
                        payload = {
                            "type": "replicate",
                            "key": key,
                            "value": value
                        }
                        await session.post(url, json=payload)
                except Exception as e:
                    logger.warning(f"Server {self.port}: Replication failed to {port}: {str(e)}")

    async def send_heartbeat(self, lb_started):
        """Send heartbeat to load balancer every 5 seconds"""
        # Wait for LB to be ready
        await lb_started.wait()
        
        while True:
            try:
                async with aiohttp.ClientSession() as session:
                    url = f'http://localhost:{self.lb_port}/heartbeat'
                    await session.post(url, json={"port": self.port})
                    logger.debug(f"Server {self.port}: Heartbeat sent")
            except Exception as e:
                logger.warning(f"Server {self.port}: Heartbeat failed - {str(e)}")
            await asyncio.sleep(5)

    async def update_replica_list(self, lb_started):
        """Update list of replica servers every 10 seconds"""
        # Wait for LB to be ready
        await lb_started.wait()
        await asyncio.sleep(2)  # Additional buffer
        
        while True:
            try:
                async with aiohttp.ClientSession() as session:
                    url = f'http://localhost:{self.lb_port}/status'
                    async with session.get(url) as resp:
                        if resp.status == 200:
                            status = await resp.json()
                            self.replica_ports = [
                                s["port"] for s in status["servers"] 
                                if s["active"] and s["port"] != self.port
                            ]
                            logger.info(f"Server {self.port}: Updated replicas {self.replica_ports}")
            except Exception as e:
                logger.warning(f"Server {self.port}: Replica update failed - {str(e)}")
            
            await asyncio.sleep(10)

    async def run(self, lb_started):
        """Run server instance"""
        app = web.Application()
        app.router.add_post('/request', self.handle_request)
        
        # Start background tasks
        asyncio.create_task(self.send_heartbeat(lb_started))
        asyncio.create_task(self.update_replica_list(lb_started))
        
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, 'localhost', self.port)
        await site.start()
        logger.info(f"Server started on port {self.port}")

# ---------------------------
# Main System Execution
# ---------------------------
async def main():
    # Create and start load balancer
    lb = LoadBalancer()
    lb_task = asyncio.create_task(lb.run())
    
    # Wait for LB to start before starting servers
    await asyncio.sleep(1)
    
    # Start minimum number of servers
    for _ in range(lb.min_servers):
        port = await lb.start_server()
        logger.info(f"Started initial server on port {port}")
    
    # Keep the system running
    await asyncio.Future()

if __name__ == '__main__':
    print("🚀 Starting distributed system...")
    print("CTRL+C to exit\n")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 System shutdown")
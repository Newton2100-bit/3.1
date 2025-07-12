# Flat Naming System
name_server = {
    "server1": "192.168.1.2",
    "server2": "192.168.1.3"
}

# Query
server = name_server.get("server1", None)
print(f"--Server one--{'\n'}IP address of server1: {server}")
print(f'--server two--{"\n"}Ip address of server2 :{name_server.get("server2")}')



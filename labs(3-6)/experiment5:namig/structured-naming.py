# Structured Naming System (Hierarchical)
name_server = {
    "region1": {
        "server1": "192.168.1.2",
        "server2": "192.168.1.3"
    },
    "region2": {
        "server3": "192.168.2.1",
        "server4": "192.168.2.2"
    }
}

# Query
server = name_server["region1"].get("server1", None)
print(f"IP address of region1 server1: {server}")


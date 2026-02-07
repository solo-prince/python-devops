def greet_user(name):
    print(f"Hello {name}, welcome to Python DevOps")

def check_server(server_name, status):
    print(f"Server {server_name} is {status}")

def disk_usage(used, total):
    percent = (used / total) * 100
    return percent


# Function calls
greet_user("Pravin")

check_server("web", "running")
check_server("db", "stopped")

usage = disk_usage(40, 100)
print("Disk usage:", usage, "%")

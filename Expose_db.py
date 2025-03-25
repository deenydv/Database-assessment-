import socket

def check_exposed_database(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((host, port))
        print(f"{RED}[VULNERABLE]{RESET} Database {host}:{port} is accessible without authentication!")
        s.close()
    except:
        print(f"{GREEN}[SAFE]{RESET} No exposed database found on {host}:{port}.")

# Common database ports
databases = {
    "MongoDB": 27017,
    "MySQL": 3306,
    "PostgreSQL": 5432,
    "Elasticsearch": 9200
}

for db, port in databases.items():
    print(f"{YELLOW}Checking {db} on localhost:{port}...{RESET}")
    check_exposed_database("127.0.0.1", port

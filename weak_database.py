import mysql.connector

def test_weak_db_credentials(host, user, password):
    try:
        conn = mysql.connector.connect(host=host, user=user, password=password)
        conn.close()
        print(f"{RED}[VULNERABLE]{RESET} Weak credentials found: {user}/{password}")
    except:
        print(f"{GREEN}[SAFE]{RESET} Credentials {user}/{password} are secure.")

# Common weak credentials
weak_users = ["root", "admin", "test", "user"]
weak_passwords = ["1234", "password", "root", "admin"]

for user in weak_users:
    for password in weak_passwords:
        test_weak_db_credentials("127.0.0.1", user, password

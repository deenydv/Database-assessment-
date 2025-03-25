import mysql.connector

def check_unencrypted_db(host, user, password):
    try:
        conn = mysql.connector.connect(host=host, user=user, password=password)
        cursor = conn.cursor()
        cursor.execute("SHOW VARIABLES LIKE 'have_ssl';")
        ssl_status = cursor.fetchone()

        if ssl_status and ssl_status[1] == "YES":
            print(f"{GREEN}[SECURE]{RESET} Database is using SSL encryption.")
        else:
            print(f"{RED}[VULNERABLE]{RESET} Database is NOT using SSL encryption!")
        conn.close()
    except:
        print(f"{YELLOW}[ERROR]{RESET} Could not check SSL encryption status.")

check_unencrypted_db("127.0.0.1", "root", "password"

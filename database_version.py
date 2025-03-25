import mysql.connector

def detect_db_version(host, user, password):
    try:
        conn = mysql.connector.connect(host=host, user=user, password=password)
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION();")
        version = cursor.fetchone()[0]
        print(f"{YELLOW}[INFO]{RESET} Database version: {version}")
        conn.close()
    except:
        print(f"{RED}[ERROR]{RESET} Could not retrieve database version.")

detect_db_version("127.0.0.1", "root", "password"

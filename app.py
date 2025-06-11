from flask import Flask
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="10.0.2.15",
        database="banco",
        user="admin",
        password="admin"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f"Hello, Flask! PostgreSQL version: {db_version}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

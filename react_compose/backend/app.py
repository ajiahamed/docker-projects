from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="mydb",
        user="postgres",
        password="postgres"
    )
    return conn

@app.route("/")
def home():
    return jsonify({"message": "Hello from backend"})

@app.route("/data")
def data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify({"db_response": result[0]})

app.run(host="0.0.0.0", port=5000)

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f"Connected to DB at {os.getenv('DB_HOST')}"

app.run(host='0.0.0.0', port=5000)
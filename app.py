from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return f"""
    <h1>Hello from Flask</h1>
    <p>Version: {os.getenv("APP_VERSION")}</p>
    """


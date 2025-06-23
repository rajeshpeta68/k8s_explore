from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    mode = os.getenv("APP_MODE", "undefined")
    log = os.getenv("LOG_LEVEL", "undefined")
    return f"<h1>App Mode: {mode}</h1><h2>Log Level: {log}</h2>"

# 🔥 Add this block to start the Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

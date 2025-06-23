from flask import Flask
import time

app = Flask(__name__)

start_time = time.time()

@app.route("/startup")
def startup():
    # simulate app that takes 20s to fully start
    if time.time() - start_time < 20:
        return "Starting up...", 500
    return "Startup complete", 200

@app.route("/healthz")
def healthz():
    return "Alive", 200

@app.route("/ready")
def ready():
    return "Ready to serve!", 200

@app.route("/")
def home():
    return "Welcome to the probe-demo app"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

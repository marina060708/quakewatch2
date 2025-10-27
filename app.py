from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

# Initialize Flask app
app = Flask(__name__)

# Attach Prometheus metrics exporter
metrics = PrometheusMetrics(app)

# Define your routes
@app.route("/")
def home():
    return "Hello from QuakeWatch2!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

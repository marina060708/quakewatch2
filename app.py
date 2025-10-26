from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from QuakeWatch2!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
from prometheus_flask_exporter import PrometheusMetrics
metrics = PrometheusMetrics(app)

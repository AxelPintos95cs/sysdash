from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

# Métricas
REQUEST_COUNT = Counter("app_requests_total", "Total de requests recibidas", ['method', 'endpoint'])
REQUEST_LATENCY = Histogram("app_request_latency_seconds", "Latencia por endpoint", ['endpoint'])

@app.before_request
def before_request():
    app.start_time = time.time()

@app.after_request
def after_request(response):
    request_latency = time.time() - app.start_time
    REQUEST_LATENCY.labels(endpoint=str(response.status_code)).observe(request_latency)
    REQUEST_COUNT.labels(method='GET', endpoint=response.status_code).inc()
    return response

@app.route("/")
def home():
    return "¡Hola desde Flask + Prometheus!"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

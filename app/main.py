from flask import Flask, jsonify, request
import os, psycopg2
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

@app.route("/db-status")
def db_status():
    try:
        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "postgres"),
            database=os.getenv("POSTGRES_DB", "app_db"),
            user=os.getenv("POSTGRES_USER", "user"),
            password=os.getenv("POSTGRES_PASSWORD", "password"),
        )
        conn.close()
        return jsonify({"status": "OK"}), 200
    except Exception as e:
        return jsonify({"status": "error", "details": str(e)}), 500
    
users = []

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Faltan campos 'name' o 'email'"}), 400
    users.append(data)
    return jsonify(data), 201

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

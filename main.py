from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI()
REQUESTS = Counter("http_requests_total", "Total HTTP Requests")

@app.get("/")
def root():
    REQUESTS.inc()
    return {"message": "Hello from test app"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

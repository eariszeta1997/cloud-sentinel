from fastapi import FastAPI, Response, status

app = FastAPI(title="Cloud Sentinel")

# Questa variabile ci permetterà di simulare un guasto (utile per i test futuri)
HEALTHY = True

@app.get("/")
def read_root():
    return {"message": "Cloud Sentinel is running. Check /health for status."}

@app.get("/health")
def health_check(response: Response):
    if HEALTHY:
        return {"status": "UP", "message": "Servizio Attivo"}
    else:
        # Se c'è un guasto, restituisce un errore 503 (Rosso)
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "DOWN", "message": "Service Unavailable"}

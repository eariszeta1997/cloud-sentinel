from fastapi import FastAPI, Response, status
from fastapi.responses import HTMLResponse

app = FastAPI(title="Cloud Sentinel")

HEALTHY = True

# Nuova rotta: Python costruisce l'HTML al volo (Server-Side Rendering)
@app.get("/", response_class=HTMLResponse)
def read_root():
    # Python decide lo stato PRIMA di creare la pagina
    if HEALTHY:
        colore = "#2ea043"  # Verde
        messaggio = "Servizio Attivo"
    else:
        colore = "#da3633"  # Rosso
        messaggio = "SERVIZIO GUASTO"

    # Python inietta le variabili nell'HTML (senza usare JavaScript!)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Questo tag HTML puro ricarica la pagina da sola ogni 5 secondi -->
        <meta http-equiv="refresh" content="5">
        <title>Cloud Sentinel - Dashboard</title>
        <style>
            body {{ background-color: #0d1117; color: #c9d1d9; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
            .dashboard {{ background-color: #161b22; padding: 40px; border-radius: 12px; text-align: center; border: 1px solid #30363d; width: 350px; }}
            .indicator {{ width: 80px; height: 80px; border-radius: 50%; margin: 0 auto 15px auto; background-color: {colore}; box-shadow: 0 0 25px {colore}; }}
            .status-text {{ font-size: 18px; font-weight: bold; color: {colore}; letter-spacing: 1px; }}
        </style>
    </head>
    <body>
        <div class="dashboard">
            <h1>🛡️ Cloud Sentinel</h1>
            <p>System Health Monitor</p>
            <div style="margin-top: 30px; padding: 20px; background-color: #0d1117; border-radius: 8px; border: 1px solid #30363d;">
                <div class="indicator"></div>
                <div class="status-text">{messaggio}</div>
            </div>
            <p style="font-size: 12px; color: #8b949e; margin-top: 20px;">(Auto-aggiornamento HTML ogni 5 secondi)</p>
        </div>
    </body>
    </html>
    """
    return html_content

# La nostra sonda originale rimane intatta per Kubernetes
@app.get("/health")
def health_check(response: Response):
    if HEALTHY:
        return {"status": "UP", "message": "Servizio Attivo"}
    else:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "DOWN", "message": "Service Unavailable"}
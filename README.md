# 🛡️ Cloud Sentinel

**Cloud Sentinel** è un microservizio leggero progettato per dimostrare metodologie di sviluppo cloud-native e l'implementazione di una pipeline DevOps completa.

Questo progetto funge da prova di concetto (PoC) per l'implementazione di health-check (sonde di vitalità) fondamentali nei sistemi distribuiti gestiti da orchestratori come Kubernetes.

## 🎯 Obiettivi del Progetto

1. **Sviluppo Standardizzato**: Realizzazione di un'API RESTful con Python e FastAPI.
2. **Affidabilità e TDD**: Implementazione di test automatici strutturati tramite Pytest.
3. **Portabilità Universale**: Isolamento dell'applicazione in container Linux leggeri con Docker.
4. **Infrastructure as Code (IaC)**: Definizione dell'infrastruttura di gestione (simulazione) con Terraform e manifesti Kubernetes.
5. **Continuous Integration (CI)**: Automazione del ciclo di test e verifica della build tramite GitHub Actions.

## 🛠️ Stack Tecnologico

- **Linguaggio**: Python 3.11+
- **Framework Web**: FastAPI / Uvicorn
- **Testing**: Pytest / HTTPX
- **Containerization**: Docker
- **Infrastruttura**: Kubernetes (manifest) / Terraform (IaC)
- **CI/CD Pipeline**: GitHub Actions

## 🚦 Endpoint Principale

Il servizio espone una sonda `/health` studiata per le *Liveness e Readiness Probe* degli orchestratori cloud.
- `GET /health` -> `200 OK` (Servizio Attivo)
- Simulazione Guasto -> `503 Service Unavailable`

# BotTele
# Telegram Bot con CI/CD en Azure ☁️🤖

Este bot de Telegram reemplaza texto en mensajes anteriores con un comando tipo `/s/original/nuevo`.

## 🐳 Tecnologías

- Python
- Docker
- Azure Container Registry (ACR)
- Azure Web App for Containers
- GitHub Actions (CI/CD)

## 🚀 Despliegue automático

Cada vez que haces push a `main`, se:

1. Construye una imagen Docker
2. Se sube a ACR
3. Se despliega en tu Web App en Azure


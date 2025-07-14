# 🖥️ System Monitoring Dashboard (Prometheus + Grafana)

Este proyecto configura un entorno completo de monitoreo de sistemas usando:

- **Prometheus** – recolecta métricas del sistema
- **Node Exporter** – expone métricas del host
- **Grafana** – visualiza métricas en un dashboard atractivo
- **Docker Compose** – todo orquestado en contenedores

---

## 📦 Tecnologías utilizadas

- Docker
- Prometheus
- Grafana
- Node Exporter
- YAML provisioning
- Linux metrics
- Provisionamiento automático de dashboards

---

### 🔐 Seguridad y producción

Este proyecto está pensado para uso local o ambientes controlados. Para producción se recomienda:

Autenticación reforzada en Grafana

HTTPS reverse proxy

Retención optimizada en Prometheus

Exportar logs y alertas

---

## Cómo levantar el proyecto

> Requiere tener [Docker](https://www.docker.com/products/docker-desktop/) y `docker compose` instalados.

```bash
git clone https://github.com/tu-usuario/system-monitoring-dashboard.git
cd system-monitoring-dashboard
docker compose up -d
```

---

## Cómo usar Grafana
Acceder a Grafana en: http://localhost:3000

Usuario: admin / Contraseña: admin (te pedirá cambiarla la primera vez)

Ya viene preconfigurado con:

Data Source: Prometheus

Dashboard: Node Exporter Full (importado automáticamente desde system-dashboard.json)

---

## Autor

🧠 Axel Pintos

💼 SysAdmin Jr. | DevOps en formación

---
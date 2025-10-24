# ⚡ Simple One-Shot Post/Get API

A lightweight **FastAPI** microservice that accepts a single JSON `POST` request and returns that same payload when queried via `GET`.  
Perfect for use with **Power Automate**, **Python scripts**, or other automations needing a quick message relay or temporary data handoff.

---

## 🚀 Features

- 📨 **Single-value cache** — stores only the most recent POST.
- ⚡ **Instant retrieval** — always returns the latest posted JSON.
- 💾 **Simple persistence** — saves to a small `latest_post.json` file.
- 🧱 **Dockerized** — easy to deploy locally or remotely.
- 🔁 **Stateless design** — no database or queues to manage.

---

## 📁 Project Structure

project-root/
│
├── app/
│ ├── main.py # FastAPI app (POST/GET endpoints)
│ ├── init.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

yaml
Copy code

---

## 🧰 Requirements

- 🐳 Docker & Docker Compose  
- (Optional) Python 3.10+ for local testing

---

## ⚙️ Setup & Run

### 🏗️ 1. Build and start with Docker Compose
```bash
docker compose up --build
🌀 2. Run in background
bash
Copy code
docker compose up -d
🧹 3. Stop and remove containers
bash
Copy code
docker compose down
🪵 4. View logs
bash
Copy code
docker compose logs -f
🌐 API Endpoints
POST /post
Stores (and overwrites) the current JSON payload.

Example

bash
Copy code
curl -X POST http://localhost:8000/post \
  -H "Content-Type: application/json" \
  -d '{
    "Title": "Lowe\'s #1720 (Pilot)",
    "Serial": "N4R01459",
    "Category": "Pilot",
    "Stakeholder": "James.Novell@sesami.io"
  }'
Response

json
Copy code
{
  "status": "stored",
  "size": 132
}
GET /get
Returns the most recently posted payload.

Example

bash
Copy code
curl http://localhost:8000/get
Response

json
Copy code
{
  "status": "ok",
  "data": {
    "Title": "Lowe's #1720 (Pilot)",
    "Serial": "N4R01459",
    "Category": "Pilot",
    "Stakeholder": "James.Novell@sesami.io"
  }
}
GET /
Displays basic service info and available routes.

💾 Data Storage
The app writes its last POST to a JSON file:

pgsql
Copy code
latest_post.json
This file is mounted to your host (see docker-compose.yml), so the data persists even if the container restarts.

🧪 Local Testing (no Docker)
bash
Copy code
pip install -r requirements.txt
cd app
uvicorn main:app --reload --port 8000
Then open http://localhost:8000 in your browser.

🧩 Example Power Automate Flow
HTTP → POST

URL: http://<your-server-ip>:8000/post

Body: JSON payload from SharePoint, Excel, or other source

HTTP → GET

URL: http://<your-server-ip>:8000/get

Use the returned JSON in subsequent steps

👤 Author
James Novell
📧 james.novell@sesami.io
⚙️ Sesami Analytics / Power Automate Integrations

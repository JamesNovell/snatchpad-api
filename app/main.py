from fastapi import FastAPI, Request
from typing import Any, Dict
import json
import os

app = FastAPI(title="Simple One-Shot Post/Get API", version="1.0")

CACHE_FILE = "latest_post.json"

def load_cache() -> Dict[str, Any]:
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_cache(data: Dict[str, Any]):
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f, indent=2)

# Load existing cache on startup
cache = load_cache()

@app.post("/post")
async def post_data(request: Request):
    """
    Accepts a single JSON payload and overwrites the existing one.
    Example:
    {
      "Title": "Lowe's #1720",
      "Serial": "N4R01459",
      "Category": "Pilot",
      "Stakeholder": "James.Novell@sesami.io"
    }
    """
    global cache
    data = await request.json()
    cache = data
    save_cache(cache)
    print("📥 Received new payload:", json.dumps(cache, indent=2))
    return {"status": "stored", "size": len(json.dumps(data))}

@app.get("/get")
async def get_data():
    """
    Returns the most recently posted JSON payload.
    """
    if not cache:
        return {"status": "empty", "message": "No data has been posted yet."}
    return {"status": "ok", "data": cache}

@app.get("/")
def root():
    return {
        "message": "Simple One-Shot Post/Get API running 🚀",
        "routes": {
            "POST": "/post",
            "GET": "/get"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
import socket
import datetime

app = FastAPI()

APP_NAME = os.getenv("APP_NAME", "Docker Web App")
APP_ENV = os.getenv("APP_ENV", "development")
START_TIME = datetime.datetime.now().isoformat(timespec="seconds")


@app.get("/", response_class=HTMLResponse)
def home():
    return f"""
    <html>
      <head><title>{APP_NAME}</title></head>
      <body style="font-family: sans-serif; max-width: 600px; margin: 40px auto;">
        <h1>{APP_NAME}</h1>
        <p><b>Environment:</b> {APP_ENV}</p>
        <p><b>Container:</b> {socket.gethostname()}</p>
        <p><b>Started:</b> {START_TIME}</p>
        <p>Try <a href="/api/info">/api/info</a> or <a href="/health">/health</a></p>
      </body>
    </html>
    """


@app.get("/api/info")
def info():
    return {"app": APP_NAME, "env": APP_ENV, "container": socket.gethostname(), "started": START_TIME}


@app.get("/health")
def health():
    return {"status": "ok"}
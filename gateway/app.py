from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI(title="Gateway (Level 2 - Forwarding / Tamper Simulation)")

RECEIVER_VERIFY_URL = "http://127.0.0.1:8001/verify"

class ForwardRequest(BaseModel):
    message: str
    signature_b64: str

@app.get("/")
def health():
    return {"status": "gateway running", "endpoints": ["/forward"]}

@app.post("/forward")
def forward(req: ForwardRequest, mode: str = "pass"):
    # mode=pass   -> forward as-is
    # mode=tamper -> modify the message, keep signature the same (attack simulation)
    out_message = req.message
    if mode == "tamper":
        out_message = req.message.replace("1000", "9000") if "1000" in req.message else (req.message + " (tampered)")

    payload = {
        "message": out_message,
        "signature_b64": req.signature_b64
    }

    r = requests.post(RECEIVER_VERIFY_URL, json=payload, timeout=10)
    r.raise_for_status()
    return {
        "gateway_mode": mode,
        "forwarded_message": out_message,
        "receiver_response": r.json()
    }

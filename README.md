# digital-signature-demo

 sender_reciever:
 ## Setup

    1. Install dependencies
    pip install fastapi uvicorn requests cryptography

    2. Generate keys
    py tools/make_keys.py

    3. Run receiver
    py -m uvicorn receiver.app:app --port 8001

    4. Run gateway
    py -m uvicorn gateway.app:app --port 8000

    5. Run sender
    py -m uvicorn sender.app:app --port 8002

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from pathlib import Path

sender_dir = Path("sender")
receiver_dir = Path("receiver")

sender_dir.mkdir(exist_ok=True)
receiver_dir.mkdir(exist_ok=True)

# Generate RSA key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Private key
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
)

# Public key
public_pem = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

(sender_dir / "private.pem").write_bytes(private_pem)
(receiver_dir / "public.pem").write_bytes(public_pem)

print("Wrote:")
print(" - sender/private.pem")
print(" - receiver/public.pem")

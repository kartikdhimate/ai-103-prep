import os

from dotenv import load_dotenv

load_dotenv()


def require(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing {name}. Copy .env.example to .env and fill it in.")
    return value

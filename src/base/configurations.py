from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self,
            client_id: Optional[str] = None,
            client_secret: Optional[str] = None,
            ):
        self.client_id = client_id if client_id is not None else get_default_client_id()
        self.client_secret = client_secret if client_secret is not None else get_default_client_secret()

def get_default_client_id() -> str:
    return os.getenv("TRAKT-SYNC_CLIENT-ID")

def get_default_client_secret() -> str:
    return os.getenv("TRAKT-SYNC_CLIENT-SECRET")
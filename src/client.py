from typing import Optional
from src.base.configurations import Config


class TraktClient:
    def __init__(self,
            config: Optional[Config] = None,
            ):
        self.config = config if config is not None else Config()
    
    @config.setter
    def config(self, config: Config):
        self._config = config
        self.client_id = config.client_id
        self.client_secret = config.client_secret
    
    @property
    def config(self) -> Config:
        return self._config
    
    def authenticate(self):
        pass
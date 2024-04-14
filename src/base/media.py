from abc import ABC
from typing import Optional, Sequence
from datetime import datetime as Datetime


class Media(ABC):
    # Media is an abstract class that represents a media, like a movie or a TV show.
    # It is the base class for all media types.
    def __init__(self,
        title: str,
        premiered: Optional[Datetime] = None,
        consumed: Optional[Sequence[Datetime]] = None,
        genres: Optional[Sequence[str]] = None,
        ):
        self.title = title
        self.premiered = premiered
        self.genres = genres if genres is not None else []
        self.consumed = consumed if consumed is not None else []
from abc import ABC
from typing import Optional, Sequence


class Media(ABC):
    # Media is an abstract class that represents a media, like a movie or a TV show.
    # It is the base class for all media types.
    def __init__(self,
        title: str,
        year: Optional[int] = None,
        genres: Optional[Sequence[str]] = [],
        ):
        self.title = title
        self.year = year
        self.genres = genres
        pass
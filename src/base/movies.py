from typing import Optional, Sequence
from datetime import datetime as Datetime

from .media import Media
from .people import Individual


class Movie(Media):
    # Movie is a class that represents a movie.
    def __init__(self,
        title: str,
        premiered: Optional[Datetime] = None,
        consumed: Optional[Sequence[Datetime]] = [],
        genres: Optional[Sequence[str]] = [],
        cast: Optional[Sequence[Individual]] = [],
        director: Optional[Individual] = None,
        ):
        super().__init__(title, premiered, consumed, genres)
        self.cast = cast
        self.director = director
        pass
    pass
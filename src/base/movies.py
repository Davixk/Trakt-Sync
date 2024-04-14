from typing import Optional, Sequence

from .media import Media
from .people import Individual


class Movie(Media):
    # Movie is a class that represents a movie.
    def __init__(self,
        title: str,
        year: Optional[int] = None,
        genres: Optional[Sequence[str]] = [],
        cast: Optional[Sequence[Individual]] = [],
        director: Optional[Individual] = None,
        ):
        super().__init__(title, year, genres)
        self.cast = cast
        self.director = director
        pass
    pass
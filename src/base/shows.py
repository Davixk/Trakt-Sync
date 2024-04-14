from .media import Media
from .people import Individual

from typing import Optional, Sequence
from datetime import datetime as Datetime


class Show(Media):
    # Show is a class that represents a TV show or series.
    def __init__(self,
        title: str,
        premiered: Optional[Datetime] = None,
        genres: Optional[Sequence[str]] = [],
        cast: Optional[Sequence[Individual]] = [],
        creator: Optional[Individual] = None,
        ):
        super().__init__(title, premiered, genres)
        self.cast = cast
        self.creator = creator
        pass
    pass

class Season:
    # Season is a class that represents a season of a TV show.
    def __init__(self,
        show: Show,
        number: int,
        title: Optional[str] = None,
        episodes: Optional[Sequence[Show]] = [],
        ):
        self.number = number
        self.episodes = episodes
        pass
    
    @property
    def episode_count(self):
        return len(self.episodes)

class Episode(Media):
    # Episode is a class that represents an episode of a TV show.
    def __init__(self,
        title: str,
        premiered: Optional[Datetime] = None,
        consumed: Optional[Sequence[Datetime]] = [],
        genres: Optional[Sequence[str]] = [],
        season: Optional[Season] = None,
        show: Optional[Show] = None,
        number: Optional[int] = None,
        ):
        super().__init__(title, premiered, consumed, genres)
        self.title = title
        self.season = season
        self.show = show
        self.number = number
        pass
    pass
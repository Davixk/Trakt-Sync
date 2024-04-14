from .media import Media
from .people import Individual

from typing import Optional, Sequence


class Show(Media):
    # Show is a class that represents a TV show or series.
    def __init__(self,
        title: str,
        year: Optional[int] = None,
        genres: Optional[Sequence[str]] = [],
        cast: Optional[Sequence[Individual]] = [],
        creator: Optional[Individual] = None,
        ):
        super().__init__(title, year, genres)
        self.cast = cast
        self.creator = creator
        pass
    pass

class Season:
    # Season is a class that represents a season of a TV show.
    def __init__(self,
        number: int,
        episodes: Optional[Sequence[Show]] = [],
        ):
        self.number = number
        self.episodes = episodes
        pass
    
    @property
    def episode_count(self):
        return len(self.episodes)

class Episode:
    # Episode is a class that represents an episode of a TV show.
    def __init__(self,
        title: str,
        season: Optional[Season] = None,
        show: Optional[Show] = None,
        number: Optional[int] = None,
        ):
        self.title = title
        self.season = season
        self.show = show
        self.number = number
        pass
    pass
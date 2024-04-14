from __future__ import annotations

from .media import Media
from .people import Individual

from typing import Optional, Sequence
from datetime import datetime as Datetime


class Show:
    # Show is a class that represents a TV show or series.
    def __init__(self,
        title: str,
        genres: Optional[Sequence[str]] = [],
        cast: Optional[Sequence[Individual]] = [],
        creator: Optional[Individual] = None,
        seasons: Optional[Sequence[Season]] = [],
        ):
        self.title = title
        self.genres = genres
        self.cast = cast
        self.creator = creator
        self.seasons = seasons

    @property
    def episode_count(self):
        return sum([season.episode_count for season in self.seasons])
    
    @property
    def season_count(self):
        return len(self.seasons)
    
    @property
    def premiered(self):
        return min([season.premiered for season in self.seasons])

class Season:
    # Season is a class that represents a season of a TV show.
    def __init__(self,
        show: Show,
        number: int,
        title: Optional[str] = None,
        episodes: Optional[Sequence[Episode]] = [],
        ):
        self.show = show
        self.number = number
        self.title = title
        self.episodes = episodes
        if self.show:
            self.show.seasons.append(self)
    
    @property
    def episode_count(self):
        return len(self.episodes)
    
    @property
    def premiered(self):
        return min([episode.premiered for episode in self.episodes])

class Episode(Media):
    # Episode is a class that represents an episode of a TV show.
    def __init__(self,
        title: str,
        premiered: Optional[Datetime] = None,
        consumed: Optional[Sequence[Datetime]] = None,
        genres: Optional[Sequence[str]] = [],
        season: Optional[Season] = None,
        show: Optional[Show] = None,
        number: Optional[int] = None,
        ):
        super().__init__(title, premiered, consumed, genres)
        self.season = season
        self.show = show
        self.number = number
        if self.season:
            self.season.episodes.append(self)
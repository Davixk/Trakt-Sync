import pandas, re
from pandas import DataFrame
from datetime import datetime

from src.base.shows import Show, Season, Episode
from src.base.movies import Movie


class Netflix:
    def read_profile_dump(self,
        file_path: str = None,
        ) -> DataFrame:
        if not file_path:
            file_path = 'data/NetflixViewingHistory.csv'

        data = pandas.read_csv(file_path)
        self.raw_data = data
        return data
    
    def get_media(self,
        data: DataFrame = None,
        ):
        if not data:
            data = self.read_profile_dump()
        
        media_list = []
        for index, row in data.iterrows():
            title = row['Title'] if not pandas.isna(row['Title']) else ""
            date = row['Date'] if not pandas.isna(row['Date']) else None
            try:
                if not title:
                    continue
                parsed_content = self.parse_content_from_title(str(title))
                if date:
                    parsed_date = datetime.strptime(date, "%m/%d/%y")
                    parsed_content.consumed.append(parsed_date)
                media_list.append(parsed_content)
            except Exception as e:
                print(f"Failed to parse title: {title}")
        return media_list

    def parse_content_from_title(self,
        title: str,
        ):
        pattern = re.compile(r"^(.*?): (Season \d+|Part \d+|Volume \d+): (.+)$")
        match = pattern.match(title)
        if match:
            show_name, season_str, episode_str = match.groups()
            if show_name:
                show = Show(title=show_name)
                if season_str:
                    season_number = int(season_str.split(' ')[1])
                    season = Season(show=show, number=season_number, title=season_str)
                    if episode_str:
                        episode = Episode(title=episode_str, show=show, season=season)
                        return episode
                    else: return season
                else: return show
            else: return None
        else:
            movie = Movie(title=title)
            return movie
import pandas, re
from pandas import DataFrame


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
        
        for title in data.Title:
            parsed_content = self.parse_content_from_title(title)
        pass

    def parse_content_from_title(self,
        title: str,
        ):
        title = title.lower()
        title = re.sub(r'[^a-zA-Z0-9\s]', '', title)
        title = title.split(' ')
        return title


if __name__ == '__main__':
    netflix = Netflix()
    media = netflix.get_media()
    pass
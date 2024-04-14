from typing import Optional


class Individual:
    # Individual is a class that represents a person.
    def __init__(self,
        name: str,
        birth_year: Optional[int] = None,
        death_year: Optional[int] = None,
        ):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year
        pass
    pass
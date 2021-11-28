# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional

# Pip
from jsoncodable import JSONCodable

# Local


# -------------------------------------------------------------------------------------------------------------------------------- #



# ----------------------------------------------------- class: TrendingToken ----------------------------------------------------- #

class TrendingToken(JSONCodable):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        address: str,
        references: int,
        visits: int
    ):
        self.address = address
        self.references = references
        self.visits = visits


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    @classmethod
    def from_dict(
        cls,
        d: dict
    ):
        try:
            return cls(
                address=d.get('dimensions').get('metric').split('/')[-1],
                references=d.get('count'),
                visits=d.get('sum').get('visits')
            )
        except:
            return None


# -------------------------------------------------------------------------------------------------------------------------------- #
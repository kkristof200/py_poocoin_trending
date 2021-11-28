# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional, List

# Pip
from ksimpleapi import Api

# Local
from .models import *

# -------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------------- class: PoocoinTrending ---------------------------------------------------- #

class PoocoinTrending(Api):

    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def get_trending_tokens(
        self,
        interval: Optional[TimeInterval] = None,
        sorting: Optional[Sorting] = None
    ) -> List[TrendingToken]:
        interval = interval or TimeInterval.T_24_hours

        res = self._post(
            url='https://api1.poocoin.app/top-requests',
            body={
                '13': 37,
                'age': interval.value
            }
        )

        try:
            results = res.json().get('data').get('viewer').get('accounts')[0].get('topPaths')

            tokens = [
                TrendingToken.from_dict(token_d)
                for token_d in results
            ]
            print(len(tokens))

            if sorting:
                tokens = sorted(tokens, key=lambda x: x.references if sorting == Sorting.ReferencesAscending else x.visits, reverse=True)

            return tokens
        except Exception as e:
            return []


# -------------------------------------------------------------------------------------------------------------------------------- #
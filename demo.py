from poocoin_trending import *

from kcu import kjson

pct = PoocoinTrending(
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    debug=True
)
tokens = pct.get_trending_tokens(interval=TimeInterval.T_30_minutes, sorting=Sorting.ReferencesAscending)
# poocoin_trending

![PyPI - package version](https://img.shields.io/pypi/v/poocoin_trending?logo=pypi&style=flat-square)
![PyPI - license](https://img.shields.io/pypi/l/poocoin_trending?label=package%20license&style=flat-square)
![PyPI - python version](https://img.shields.io/pypi/pyversions/poocoin_trending?logo=pypi&style=flat-square)
![PyPI - downloads](https://img.shields.io/pypi/dm/poocoin_trending?logo=pypi&style=flat-square)

![GitHub - last commit](https://img.shields.io/github/last-commit/kkristof200/py_poocoin_trending?style=flat-square)
![GitHub - commit activity](https://img.shields.io/github/commit-activity/m/kkristof200/py_poocoin_trending?style=flat-square)

![GitHub - code size in bytes](https://img.shields.io/github/languages/code-size/kkristof200/py_poocoin_trending?style=flat-square)
![GitHub - repo size](https://img.shields.io/github/repo-size/kkristof200/py_poocoin_trending?style=flat-square)
![GitHub - lines of code](https://img.shields.io/tokei/lines/github/kkristof200/py_poocoin_trending?style=flat-square)

![GitHub - license](https://img.shields.io/github/license/kkristof200/py_poocoin_trending?label=repo%20license&style=flat-square)

## Description



## Install

~~~~bash
pip install poocoin_trending
# or
pip3 install poocoin_trending
~~~~

## Usage

~~~~python
from poocoin_trending import *

from kcu import kjson

pct = PoocoinTrending(
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    debug=True
)
tokens = pct.get_trending_tokens(interval=TimeInterval.T_30_minutes, sorting=Sorting.ReferencesAscending)
~~~~

## Dependencies

[jsoncodable](https://pypi.org/project/jsoncodable), [kcu](https://pypi.org/project/kcu), [ksimpleapi](https://pypi.org/project/ksimpleapi)
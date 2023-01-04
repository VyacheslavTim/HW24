import re
from typing import Iterable, Any, Iterator, List, Set


def filter_query(param: str, data: Iterable[str]) -> Iterator[str]:
    return filter(lambda x: param in x, data)


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> Set[str]:
    return set(data)


def limit_query(param: str, data: Iterable[str]) -> List[str]:
    limit: int = int(param)
    return list(data)[:limit]


def map_query(param: str, data: Iterable[str]) -> Iterator[str]:
    column_number: int = int(param)
    return map(lambda x: x.split('')[column_number], data)


def sort_query(param: str, data: Iterable[str]) -> List[str]:
    return sorted(data, reverse=param == 'desc')


def regex_query(param: str, data: Iterable[str]) -> Iterator[str]:
    pattern = re.compile(param)
    return filter(lambda x: re.search(pattern, x), data)

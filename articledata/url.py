from hashlib import sha1
from functools import cached_property
from typing import Any, List, Optional, Set, Tuple, Union, Generator, Callable
from urllib.parse import urlencode, urljoin, urlparse, parse_qsl, ParseResult


class URL(object):
    def __init__(self, url: str) -> None:
        if isinstance(url, URL):
            url = url.url
        self.url = url

    @cached_property
    def parsed(self) -> ParseResult:
        return urlparse(self.url)

    @cached_property
    def domain(self) -> str:
        domain = self.parsed.hostname or "localhost"
        return domain.strip(".").lower()

    @cached_property
    def scheme(self) -> str:
        if self.parsed.scheme is None or not len(self.parsed.scheme):
            return "http"
        return self.parsed.scheme.lower().strip()

    def clean(self, query_ignore: Set[str]) -> "URL":
        parsed = self.parsed._replace(fragment="")
        parsed = parsed._replace(netloc=parsed.netloc.lower())
        cleaned_query: List[Tuple[str, str]] = []
        for key, value in parse_qsl(parsed.query):
            if key not in query_ignore:
                cleaned_query.append((key, value))
        parsed = parsed._replace(query=urlencode(cleaned_query))
        return URL(parsed.geturl())

    @cached_property
    def id(self) -> str:
        parsed = self.parsed._replace(fragment="")
        parsed = parsed._replace(netloc=parsed.netloc.lower())
        parsed = parsed._replace(path=parsed.path.rstrip("/"))
        parsed = parsed._replace(scheme="http")
        norm = parsed.geturl().encode("utf-8")
        return sha1(norm).hexdigest()

    def join(self, text: str) -> Optional["URL"]:
        try:
            return URL(urljoin(self.url, text))
        except (TypeError, ValueError):
            return None

    @classmethod
    def __get_validators__(
        cls,
    ) -> Generator[Callable[[Any], Union[str, "URL"]], None, None]:
        yield cls.validate

    @classmethod
    def validate(cls, text: Any) -> Union[str, "URL"]:
        if not isinstance(text, (str, URL)) or text is None:
            raise TypeError("URL is not a string: %r", type(text))
        return text

    def __str__(self) -> str:
        return self.url

    def __repr__(self) -> str:
        return self.url

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, URL):
            return other.id == self.id
        return str(other) == self.url

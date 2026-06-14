from dataclasses import dataclass


@dataclass
class WordResult:
    query: str
    title: str
    grammar: str
    short_text: str
    full_text: str | None
    is_truncated: bool
    source_url: str
    definitions: list[str]

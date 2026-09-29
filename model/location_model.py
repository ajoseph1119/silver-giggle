from dataclasses import dataclass


@dataclass
class Location:
    name: str
    search_terms: list[str]


UNITED_STATES = Location(
    name="United States",
    search_terms=[
        "United States",
        "Remote",
    ],
)

REMOTE = Location(
    name="Remote",
    search_terms=[
        "Remote",
        "United States",
    ],
)

NEW_YORK = Location(
    name="New York",
    search_terms=[
        "New York",
        "NYC",
    ],
)
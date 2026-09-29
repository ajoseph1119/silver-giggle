from dataclasses import dataclass


@dataclass
class Experience:
    name: str
    search_terms: list[str]


JUNIOR = Experience(
    name="Junior",
    search_terms=[
        "Junior",
        "Entry Level",
        "Entry-Level",
        "New Grad",
        "New Graduate",
        "Recent Graduate",
        "Early Career",
        "Early-Career",
        "Associate",
        "Engineer I",
        "Software Engineer I",
        "Developer I",
        "Level 1",
        "IC1",
        "0-1 years",
        "0-2 years",
        "1-2 years",
        "0-3 years",
        "1-3 years",
        "No experience",
        "No experience required",
    ],
)
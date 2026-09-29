from dataclasses import dataclass


@dataclass
class JobTitle:
    name: str
    search_terms: list[str]


SOFTWARE_ENGINEER = JobTitle(
    name="Software Engineer",
    search_terms=[
        "Software Engineer",
        "Software Engineer I",
        "Associate Software Engineer",
        "Junior Software Engineer",
        "Entry Level Software Engineer",
        "New Grad Software Engineer",
        "Software Developer",
        "Software Developer I",
        "Junior Software Developer",
        "Associate Software Developer",
        "Backend Engineer",
        "Backend Software Engineer",
        "Frontend Engineer",
        "Frontend Software Engineer",
        "Full Stack Engineer",
        "Full Stack Software Engineer",
        "Application Engineer",
        "Application Developer",
        "Systems Engineer",
        "Platform Engineer",
    ],
)
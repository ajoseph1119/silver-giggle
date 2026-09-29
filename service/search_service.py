import os
from urllib.parse import urlparse

import serpapi
from dotenv import load_dotenv


load_dotenv(override=True)


class SearchService:

    SITES = {
        "Greenhouse": "boards.greenhouse.io",
        "Lever": "jobs.lever.co",
        "Ashby": "jobs.ashbyhq.com",
        "Workable": "apply.workable.com",
        "Workday": "myworkdayjobs.com",
    }

    def __init__(self):
        self.api_key = os.getenv("SERPAPI_API_KEY")

        if not self.api_key:
            raise ValueError("SERPAPI_API_KEY is not set")

        self.client = serpapi.Client(
            api_key=self.api_key
        )

    @staticmethod
    def _or_group(terms: list[str]) -> str:
        formatted_terms = []

        for term in terms:
            if " " in term:
                formatted_terms.append(f'"{term}"')
            else:
                formatted_terms.append(term)

        return "(" + " OR ".join(formatted_terms) + ")"

    def build_query(
        self,
        job_titles: list[str],
        experience_terms: list[str],
        site: str,
    ) -> str:

        title_group = self._or_group(job_titles)
        experience_group = self._or_group(experience_terms)

        return (
            f"site:{site} "
            f"{title_group} "
            f"{experience_group}"
        )

    def search(
        self,
        query: str,
        location: str = "United States",
        start: int = 0,
    ) -> dict:

        results = self.client.search({
            "engine": "google",
            "q": query,

            # United States Google results
            "location": location,
            "gl": "us",
            "hl": "en",

            # Results from the past week
            "tbs": "qdr:w",

            # Pagination
            "start": start,

            # Include omitted/duplicate results where possible
            "filter": "0",
        })

        return results

    def search_all_sites(
        self,
        job_titles: list[str],
        experience_terms: list[str],
        max_pages: int = 3,
    ) -> list[dict]:

        all_jobs = []

        for source, site in self.SITES.items():

            print(f"\nSearching {source}...")
            print(f"Site: {site}")

            query = self.build_query(
                job_titles=job_titles,
                experience_terms=experience_terms,
                site=site,
            )

            print(f"Query: {query}")

            for page in range(max_pages):

                start = page * 10

                print(
                    f"  Searching page {page + 1} "
                    f"(start={start})..."
                )

                results = self.search(
                    query=query,
                    start=start,
                )

                jobs = self.parse_results(results)

                if not jobs:
                    print("  No more results.")
                    break

                all_jobs.extend(jobs)

                print(
                    f"  Found {len(jobs)} results"
                )

                # Stop if Google has no more pages
                pagination = results.get("serpapi_pagination", {})

                if "next_link" not in pagination:
                    break

        return self.deduplicate(all_jobs)

    def parse_results(self, data: dict) -> list[dict]:
        jobs = []

        for result in data.get("organic_results", []):

            url = result.get("link", "")

            jobs.append({
                "title": result.get("title", ""),
                "company": self.extract_company(url),
                "location": "",
                "url": url,
                "snippet": result.get("snippet", ""),
                "source": self.extract_source(url),
            })

        return jobs

    def deduplicate(self, jobs: list[dict]) -> list[dict]:
        seen = set()
        unique_jobs = []

        for job in jobs:
            url = job["url"].rstrip("/")

            if url in seen:
                continue

            seen.add(url)
            unique_jobs.append(job)

        return unique_jobs

    def extract_company(self, url: str) -> str:

        parsed = urlparse(url)
        hostname = parsed.hostname or ""
        hostname = hostname.lower()

        path_parts = parsed.path.strip("/").split("/")

        if not path_parts or not path_parts[0]:
            return ""

        # Greenhouse
        if "greenhouse.io" in hostname:
            return path_parts[0]

        # Lever
        if "lever.co" in hostname:
            return path_parts[0]

        # Ashby
        if "ashbyhq.com" in hostname:
            return path_parts[0]

        # Workable
        if "workable.com" in hostname:
            return path_parts[0]

        # Workday
        if "myworkdayjobs.com" in hostname:
            return path_parts[0]

        return ""

    def extract_source(self, url: str) -> str:

        hostname = urlparse(url).hostname or ""
        hostname = hostname.lower()

        if "greenhouse" in hostname:
            return "Greenhouse"

        if "lever" in hostname:
            return "Lever"

        if "ashby" in hostname:
            return "Ashby"

        if "workday" in hostname:
            return "Workday"

        if "workable" in hostname:
            return "Workable"

        return hostname
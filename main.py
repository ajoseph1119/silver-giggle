from model.experience_model import JUNIOR
from model.job_title_model import SOFTWARE_ENGINEER

from service.search_service import SearchService
from service.spreadsheet_service import SpreadsheetService


def main():
    search = SearchService()

    jobs = search.search_all_sites(
        job_titles=SOFTWARE_ENGINEER.search_terms,
        experience_terms=JUNIOR.search_terms,
        max_pages=3,
    )

    print()
    print(f"Total unique jobs found: {len(jobs)}")

    spreadsheet = SpreadsheetService()

    spreadsheet.create(
        jobs,
        filename="software_engineer_jobs.xlsx"
    )


if __name__ == "__main__":
    main()
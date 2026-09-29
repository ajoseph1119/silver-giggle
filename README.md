# silver-giggle

silver-giggle is a Python job search tool that finds junior and entry-level software engineering jobs across multiple ATS platforms.

## Supported Platforms

* Greenhouse
* Lever
* Ashby
* Workable
* Workday

## Features

* Searches Google using SerpApi
* Searches for junior and entry-level roles
* Filters results to the past week
* Searches multiple ATS platforms
* Removes duplicate jobs
* Exports results to Excel

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
SERPAPI_API_KEY=your_api_key
```

Run the application:

```bash
python main.py
```

Results are exported to:

```text
jobs.xlsx
```

## Requirements

* Python 3.10+
* SerpApi API key
* Internet connection

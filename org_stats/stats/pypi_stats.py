import json

import pypistats
from httpx import HTTPStatusError


def run(repos):
    downloads = 0
    for repo in repos:
        try:
            pypi_downloads = pypistats.overall(
                repo, mirrors=False, format="json"
            )
            pypi_downloads = json.loads(pypi_downloads)["data"][0]["downloads"]
            downloads = downloads + pypi_downloads
        except HTTPStatusError:
            pass

    return int(downloads / 6)  # per month

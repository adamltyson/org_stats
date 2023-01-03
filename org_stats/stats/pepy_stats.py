import json
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def run(repos):
    downloads = 0
    for repo in repos:
        try:
            pepy_downloads = get_downloads(repo)
            downloads = downloads + pepy_downloads
            print(repo)
            print(pepy_downloads)
        except HTTPError:
            pass

    return downloads


def get_downloads(repo):
    pepy_url = f"https://api.pepy.tech/api/v2/projects/{repo}"
    req = Request(url=pepy_url, headers={"User-Agent": "Mozilla/5.0"})
    webpage = urlopen(req).read()
    pepy_json = json.loads(webpage)
    total_downloads = pepy_json["total_downloads"]
    return total_downloads

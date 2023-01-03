import json
import urllib

from github import Github


def get_contributors(repo):
    contributors = []
    try:
        with urllib.request.urlopen(repo.contributors_url) as url:
            contributors_json = json.load(url)
            for contributor in contributors_json:
                contributors.append(contributor["login"])
                return contributors
    except urllib.error.HTTPError:
        return []


def run(github_token, organisation):
    g = Github(github_token)

    org = g.get_organization(organisation)
    org.login

    repos = []
    stars = 0
    contributors = []
    for repo in org.get_repos():
        print(repo.name)
        try:
            repos.append(repo.name)
        except AttributeError:
            pass
        stars = stars + repo.stargazers_count
        contributors.extend(get_contributors(repo))

    contributor_number = len(set(contributors))

    return repos, stars, contributor_number

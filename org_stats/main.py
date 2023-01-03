import typer

from org_stats.stats import github_stats, pepy_stats, pypi_stats


def main(github_token: str, organisation: str = "brainglobe"):
    repos, stars, contributors = github_stats.run(github_token, organisation)
    pypi_monthly_downloads = pypi_stats.run(repos)
    pepy_overall_downloads = pepy_stats.run(repos)

    print(stars, contributors, pypi_monthly_downloads, pepy_overall_downloads)


if __name__ == "__main__":
    typer.run(main)

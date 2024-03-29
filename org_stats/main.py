import typer

from org_stats.stats import github_stats, pepy_stats, pypi_stats


def main(organisation: str, github_token: str):
    repos, stars, contributors = github_stats.run(github_token, organisation)
    pypi_monthly_downloads = pypi_stats.run(repos)
    pepy_overall_downloads = pepy_stats.run(repos)

    print(
        f"Total stars: {stars}, "
        f"Total contributors: {contributors}, "
        f"Monthly downloads: {pypi_monthly_downloads}, "
        f"Total downloads: {pepy_overall_downloads}"
    )


def run():
    typer.run(main)


if __name__ == "__main__":
    run()

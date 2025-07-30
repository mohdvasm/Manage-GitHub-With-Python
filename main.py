"""To delete forks through API"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")
USERNAME = os.getenv("USERNAME")

# Get all your forked repos
URL = f"https://api.github.com/users/{USERNAME}/repos"

repos_to_delete = [
    "repo/name/to/delete"
]


def list_forked_repos():
    """List forked repos
    """
    github_response = requests.get(
    URL, auth=(USERNAME, TOKEN), params={"per_page": 100}, timeout=30
    )

    forked_repos = [repo['full_name'] for repo in github_response.json() if repo['fork']]

    return forked_repos


def delete_forked_repos(list_of_repos: list[str]):
    """Delete forked repose

    Args:
        list_of_repos (list[str]): list of repos
    """
    for repo in list_of_repos:
        repo_base = f"https://api.github.com/repos/{repo}"
        delete_response = requests.delete(repo_base, auth=(USERNAME, TOKEN), timeout=30)

        if delete_response.status_code == 204:
            print(f"✅ Deleted: {repo}")
        else:
            print(
                f"❌ Failed to delete {repo}: {delete_response.status_code} - {delete_response.text}"
            )


if __name__ == "__main__":
    print("Testing")

    # List forked repos
    # print(list_forked_repos())

    # Delete repos
    # delete_forked_repos(
    #     repos_to_delete
    # )

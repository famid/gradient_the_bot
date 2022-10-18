from github.service import GithubService


def create_git_repo_and_push_project(repo_name: str, is_private: bool) -> dict:
    git_create_response = GithubService(repo_name, is_private)

    push_repository_response = git_create_response.push_repository()
    if not push_repository_response['success']:
        return push_repository_response

    set_local_repository_response = git_create_response.set_local_repository()
    if not set_local_repository_response['success']:
        return set_local_repository_response

    return set_local_repository_response


if __name__ == "__main__":
    pass

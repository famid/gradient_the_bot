import subprocess
import os
from laravel_project_builder.run import build_laravel_project
from github.run import create_git_repo_and_push_project


def set_project_name() -> str:
    project_name = input("Write the project name: ")

    if not project_name:
        raise ValueError("Project name cannot be empty!!")
    if is_directory_exits(project_name):
        raise ValueError("This project name already exits")

    return project_name
    pass


def is_directory_exits(directory_name):
    is_directory_exist = subprocess.run(f"cd; ls {directory_name}", shell=True, text=True, capture_output=True)
    return True if is_directory_exist.returncode == 0 else False
    pass


database_credentials = {
    'DB_DATABASE': '',
    'DB_USERNAME': '',
    'DB_PASSWORD': ''
}


def set_database_credential() -> None:
    for credential in database_credentials:
        os.environ[credential] = input(f"{credential}: ")


def run() -> dict:
    project_name = set_project_name()
    set_database_credential()

    build_project_response = build_laravel_project(project_name)
    if not build_project_response['success']:
        return build_project_response

    git_repository_response = create_git_repo_and_push_project(project_name, True)
    if not git_repository_response['success']:
        return git_repository_response

    return git_repository_response


if __name__ == "__main__":
    run()

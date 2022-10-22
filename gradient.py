import subprocess
from gradient.build_project import BuildProject
from github.run import create_git_repo_and_push_project
from settings import APP_LIST


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


def get_project_type():
    for idx, app in enumerate(APP_LIST):
        print(idx, ". ", app)
    user_option = input("Type the app name: ")
    if user_option not in APP_LIST:
        print("You must choose the option below list!!")
        get_project_type()

    return user_option


def run() -> dict:
    project_type = get_project_type()
    project_name = set_project_name()

    project = BuildProject(project_name, project_type)

    project_create_response = project.build_project()
    if not project_create_response['success']:
        return project_create_response

    git_repository_response = create_git_repo_and_push_project(project_name, True)
    if not git_repository_response['success']:
        return git_repository_response

    return git_repository_response


if __name__ == "__main__":
    app_response = run()
    print(f"{app_response['success']}, {app_response['message']}")

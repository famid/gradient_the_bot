from laravel_project_builder.project_builder import ProjectBuilder
import os

database_credentials = {
    'DB_DATABASE': '',
    'DB_USERNAME': '',
    'DB_PASSWORD': ''
}


def set_database_credential() -> None:
    for credential in database_credentials:
        os.environ[credential] = input(f"{credential}: ")


def build_laravel_project(project_name: str):
    try:
        set_database_credential()
    except Exception as err:
        return dict(success=False, message=str(err))

    laravel_app = ProjectBuilder(project_name)

    laravel_app_build_response = laravel_app.build_project()
    if not laravel_app_build_response['success']:
        return laravel_app_build_response

    return laravel_app_build_response

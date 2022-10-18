from laravel_project_builder.project_builder import ProjectBuilder


def build_laravel_project(project_name: str):
    laravel_app = ProjectBuilder(project_name)

    laravel_app_build_response = laravel_app.build_project()
    if not laravel_app_build_response['success']:
        return laravel_app_build_response

    return laravel_app_build_response
    pass

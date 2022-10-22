from react_project_builder.project_builder import ProjectBuilder


def build_react_project(project_name: str) -> dict:
    """

    @param project_name:
    @return: dict
    """
    react_app = ProjectBuilder(project_name)

    react_app_build_response = react_app.build_project()
    if not react_app_build_response['success']:
        return react_app_build_response

    return react_app_build_response
    pass

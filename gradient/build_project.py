from laravel_project_builder.run import build_laravel_project
from react_project_builder.run import build_react_project


class BuildProject:

    def __init__(self, project_name: str, project_type: str):
        """

        @param project_name:
        @param project_type:
        """
        self.project_name = project_name
        self.project_type = project_type

    def build_project(self) -> dict:
        """

        @return: dict
        """
        if self.project_type == 'React':
            return build_react_project(self.project_name)
        elif self.project_type == "Laravel":
            return build_laravel_project(self.project_name)

        return dict(success=False, message="Something went wrong!!")


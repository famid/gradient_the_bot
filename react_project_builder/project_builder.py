import subprocess


class ProjectBuilder:
    """
        ProjectBuilder
    """

    def __init__(self, project_name: str):
        """

        :param project_name:
        """
        self.project_name = project_name

    def build_project(self) -> dict:
        """

        :return:
        """
        project_build_response = self.__build_project_by_npm()
        if not project_build_response['success']:
            return project_build_response

        return dict(success=True, message="React project is built successfully")

    def __build_project_by_npm(self) -> dict:
        """

        :return:
        """
        npm_command = f"npx create-react-app {self.project_name}"

        create_project_response = subprocess.run(f"cd; {npm_command}", shell=True, text=True, capture_output=True)
        if not create_project_response.returncode == 0:
            return dict(success=False, message=f"{create_project_response.stderr}")

        return dict(success=True, message="Project is created successfully")

import subprocess
from laravel_project_builder.set_env import SetEnv


class ProjectBuilder:
    """
        ProjectBuilder
    """

    def __init__(self, project_name: str):
        """

        :param project_name:
        """
        self.project_name = project_name
        self.set_env = SetEnv(self.project_name)

    def build_project(self) -> dict:
        """

        :return:
        """
        project_build_response_by_composer = self.__build_project_by_composer()
        if not project_build_response_by_composer['success']:
            return project_build_response_by_composer

        env_file_response = self.set_env.create_file()
        if not env_file_response['success']:
            return env_file_response

        database_credential_response = self.set_env.set_database_credentials()
        if not database_credential_response['success']:
            return database_credential_response

        return dict(success=True, message="Laravel project is built successfully")

    def __build_project_by_composer(self) -> dict:
        """

        :return:
        """
        composer_command = f"composer create-project laravel/laravel {self.project_name}"

        create_project_response = subprocess.run(f"cd; {composer_command}", shell=True, text=True, capture_output=True)
        if not create_project_response.returncode == 0:
            return dict(success=False, message=f"{create_project_response.stderr}")

        return dict(success=True, message="Project is created successfully")

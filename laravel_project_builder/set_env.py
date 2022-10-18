import subprocess
import fileinput
import os
from settings import ROOT_PATH


class SetEnv:
    def __init__(self, project_name):
        self.project_name = project_name
        self.database_credentials = {
            'DB_DATABASE': os.environ['DB_DATABASE'],
            'DB_USERNAME': os.environ['DB_USERNAME'],
            'DB_PASSWORD': os.environ['DB_PASSWORD']
        }
        self.env_file_path = f"{ROOT_PATH}{self.project_name}/.env"

    def create_file(self) -> dict:
        """

        :return:
        """
        if self.__is_env_file_exits():
            return dict(success=True, message="env file is created successfully")
        try:
            response = subprocess.run(f"cd; cp {self.project_name}/.env.example {self.project_name}/.env", shell=True,
                                      capture_output=True)
            if response.returncode == 0:
                return dict(success=False, message=f"{response.stderr}")
            return dict(success=True, message="env file is created successfully")

        except Exception as err:
            return dict(success=False, message=str(err))

    def __is_env_file_exits(self) -> bool:
        """

        :return:
        """
        is_file_exits = subprocess.run(f"cd; ls {self.project_name}/.env", shell=True, text=True, capture_output=True)

        return True if is_file_exits.returncode == 0 else False

    def set_database_credentials(self) -> dict:
        try:
            env_file = fileinput.input(self.env_file_path, inplace=True)
            for line in env_file:
                for key in self.database_credentials:
                    if key in line:
                        print()
                        line = f"{key}={self.database_credentials[key]}"
                print(line, end="")
            env_file.close()

            return dict(success=True, message="Database credential is set successfully")
        except Exception as err:
            return dict(success=False, message=str(err))

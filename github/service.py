from typing import Dict

import requests
import os
import json
from settings import GITHUB_ACCESS_TOKEN, GITHUB_USERNAME, GITHUB_SSH_URL, ROOT_PATH


class GithubService:
    """
        GithubService
    """
    API_URL: str = "https://api.github.com"
    PUSH_API_URL: str = API_URL + "/user/repos"
    __headers: Dict[str, str] = {
        'Authorization': 'token ' + GITHUB_ACCESS_TOKEN,
        'Accept': "application/vnd.github.v3+json"
    }

    def __init__(self, repository_name: str, is_private: bool):
        """

        :param repository_name:
        :param is_private:
        """
        self.repository_name = repository_name
        self.is_private = is_private

    def push_repository(self) -> dict:
        """

        :return:
        """
        try:
            response = requests.post(self.PUSH_API_URL, data=self.__create_payload(), headers=self.__headers)
            print(response.content.decode())

            return dict(success=True, message="Github repository has been created")
        except requests.exceptions.RequestException as err:
            return dict(success=False, message=str(err))

    def __create_payload(self) -> object:
        """

        :return:
        """
        return json.dumps({'name': self.repository_name, 'private': self.is_private})

    def set_local_repository(self) -> dict:
        """

        :return:
        """
        try:
            os.chdir(ROOT_PATH)
            os.system(f'mkdir {self.repository_name}')
            os.chdir(ROOT_PATH + self.repository_name)
            os.system("git init")
            os.system("touch README.md")
            os.system("git add . && git commit -m 'Initial Commit'")
            os.system("git branch -M master")
            os.system(f"{GITHUB_SSH_URL}{GITHUB_USERNAME}/{self.repository_name}.git")
            os.system("git push -u origin master")

            return dict(success=True, message="Commit and Push changes")
        except FileExistsError as err:
            # raise SystemExit(err)
            return dict(success=False, message=str(err))

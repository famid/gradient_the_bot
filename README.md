```
The tasks this tool will automate:
-----------------------------------
1. It can create both new Laravel or React project.
2. For Laravel, Generate .env file and set database credential on .env file
3. Will init git in the project and create a README.md file
4. Commit the changes
5. Create a repository with the project name in github
6. Add remote origin in your local git directory

```

```
Purpose:
--------
I had to do all this every time I start a Laravel project. 
I want my life to be more easier.

```

```
Future improvement:
-------------------
1. Same automated tasks for Python [Flask, Django] and other FrameWork 
2. integrating Gitlab API as I have integrated only Github API.

```

```
Requirements:
-------------
1. python3
2. pip
3. venv
4. git
5. OS must be Linux. I have no place for windows in my heart.

For Laravel:
1. php 
2. composer

For React:
1. node
2. npm 

```

```
Project Tree:
-------------


.
├── github
│   ├── __init__.py
│   ├── run.py
│   └── service.py
├── gradient
│   ├── build_project.py
│   └── __init__.py
├── gradient.py
├── laravel_project_builder
│   ├── __init__.py
│   ├── project_builder.py
│   ├── run.py
│   └── set_env.py
├── react_project_builder
│   ├── __init__.py
│   ├── project_builder.py
│   └── run.py
├── README.md
├── requirements.txt
└── settings.py
└── .env


```

```
Installation:
--------------
1. lets make a new directory somewhere in your computer. You know, just to make 
things clean. Run:

$ mkdir python_projects && cd python_projects

2. Assure you have python3, pip and venv. There is tons of resource to install 
those. Go get your tigers

3. now run this command bellow to make a virtualenv for your project.

$ python3 -m venv gradient_bot_env

4. Activate your venv

$ . source gradient_bot_env/bin/activate

5. Lets get into our venv 
 
$ cd gradient_bot_env

6. Clone the repo and Install all dependencies from our requirements.txt file

$ pip3 install -r requirements.txt

7. create .env file and set this variables:
GITHUB_ACCESS_TOKEN=< your github personal accerss token >
GITHUB_USERNAME=<your github username>
ROOT_PATH="your root path"

8. Run gradient.py file.
$ python gradient.py or python3 gradient.py

9. Type the project type. Laravel or React
10. Then imput the project name
11. For Laravel, input the database credentials if you want
```
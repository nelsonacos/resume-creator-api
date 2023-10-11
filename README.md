<div id="top"></div>

<p align="center">
    <a href="https://github.com/nelsonacos/resume-creator-api/graphs/contributors">
        <img src="https://img.shields.io/github/contributors/nelsonacos/resume-creator-api.svg?style=for-the-badge" alt="GitHub contributors">
    </a>
    <a href="https://github.com/nelsonacos/resume-creator-api/issues">
        <img src="https://img.shields.io/github/issues/nelsonacos/resume-creator-api?style=for-the-badge" alt="GitHub issues">
    </a>
    <a href="https://github.com/tu-usuario/resume-creator-api/network">
        <img src="https://img.shields.io/github/forks/nelsonacos/resume-creator-api?style=for-the-badge" alt="GitHub forks">
    </a>
    <a href="https://github.com/tu-usuario/resume-creator-api/stargazers">
        <img src="https://img.shields.io/github/stars/nelsonacos/resume-creator-api?style=for-the-badge" alt="GitHub stars">
    </a>
    <a href="https://github.com/nelsonacos/resume-creator-api/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/nelsonacos/resume-creator-api?style=for-the-badge" alt="GitHub license">
    </a>
</p>

<br />
<div align="center">
  <h3 align="center">Resume Creator API</h3>
  <p align="center">
    API for generating resumes easily
    <br />
    <br />
    <a href="http://localhost:8000/resume/docs/"><strong>Explore the documentation</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    ·
    <a href="https://github.com/nelsonacos/resume-creator-api/issues">Report a Bug</a>
    ·
    <a href="https://github.com/nelsonacos/resume-creator-api/issues">Request a Feature</a>
  </p>
</div>
<br />

<p align="center">
    <a href="https://github.com/nelsonacos/resume-creator-api">
        <img src="https://img.shields.io/badge/django-black?style=for-the-badge&logo=django" alt="Django">
    </a>
    <a href="https://github.com/nelsonacos/resume-creator-api">
        <img src="https://img.shields.io/badge/django%20rest%20framework-black?style=for-the-badge&logo=Django%20REST%20Framework" alt="Django REST Framework">
    </a>
    <a href="https://github.com/nelsonacos/resume-creator-api">
        <img src="https://img.shields.io/badge/docker-black?style=for-the-badge&logo=docker" alt="Docker">
    </a>
    <a href="https://github.com/nelsonacos/resume-creator-api">
        <img src="https://img.shields.io/badge/postgres-black?style=for-the-badge&logo=postgresql" alt="Postgres">
    </a>
</p>


## Getting Started

1. Clone the repository

    ```sh
    git clone https://github.com/nelsonacos/resume-creator-api.git
    ```

2. Open the command line and navigate to the project folder

    ```sh
    cd resume-creator-api
    ```
2. Create the `.env` file to configure the environment variables

    ```sh
    # Unix System
    cat .env.example > .env

    # Windows System
    copy .env.example .env
    ```
3. Configure environment variables

    ```sh
    # Use a new secret key in production
    DJANGO_SECRET_KEY="django-insecure-8ps&h4snq(-)$$@f-3vhp&dk7)hf@dnd19(4q_a+im^926hxu_"

    # Will be False if set to an empty string
    DJANGO_DEBUG=""

    # Postgres configuration
    DATABASE_HOST=db # should be the name defined in the docker-compose.yml file for the postgres service
    DATABASE_USER=postgres
    DATABASE_PASSWORD=password
    DATABASE_NAME=resume
    ```
<p align="right">(<a href="#top">back to top</a>)</p>

## Starting the Project with Docker Compose

```sh
docker-compose build && docker-compose up
```
Open http://localhost:8000/resume/api/v1/ with your browser to see the result.

Visit the documentation http://localhost:8000/resume/docs/

<p align="right">(<a href="#top">back to top</a>)</p>

## Starting the project in a virtual python environment

### Prerequisites

[Python Installation](https://www.python.org/downloads/)

1. Update package repositories

    ```sh
    sudo apt update
    ```
2. Install the package software-properties-common

    ```sh
    # allows adding a PPA (Personal Package Archive) repository needed to install Python 3
    sudo apt install software-properties-common
    ```
3. Adds the deadsnakes PPA repository

    ```sh
    # contains different versions of Python
    sudo add-apt-repository ppa:deadsnakes/ppa
    ```
4. Update the package repositories again to make the new repository available.

    ```sh
    sudo apt update
    ```
5. Install python3

    ```sh
    sudo apt install python3
    ```
6. Verify the python installation

    ```sh
    python3 --version
    ```
    Nota: These steps may vary depending on the operating system you are using. If you are using another operating system, such as macOS or Windows, the steps to install Python 3.10 may be different.

7. Create a postgres container

    [Postgres Installation](https://www.postgresql.org/download/)

    ```sh
    docker run --name db -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres
    ```
8. Access the container interactively

    ```sh
    docker exec -it db psql -U postgres
    ```
9. Create a new database

    ```sh
    CREATE DATABASE resume;
    ```
10. List databases

    ```sh
    \l
    ```
11. To exit the Postgres

    ```sh
    \q
    ```
12. Clone the repository

    ```sh
    git clone https://github.com/nelsonacos/resume-creator-api.git
    ```

13. Open the command line and navigate to the project folder

    ```sh
    cd resume-creator-api
    ```
14. Create the `.env` file to configure the environment variables

    ```sh
    # Unix System
    cat .env.example > .env

    # Windows System
    copy .env.example .env
    ```
15. Configure environment variables

    ```sh
    # Use a new secret key in production
    DJANGO_SECRET_KEY="django-insecure-8ps&h4snq(-)$$@f-3vhp&dk7)hf@dnd19(4q_a+im^926hxu_"

    # Will be False if set to an empty string
    DJANGO_DEBUG=True

    # Postgres configuration
    DATABASE_HOST=localhost
    DATABASE_USER=postgres
    DATABASE_PASSWORD=password
    DATABASE_NAME=resume
    ```
16. Create a virtual environment (optional but recommended)

    ```sh
    python3 -m venv venv
    ```
17. Activate virtual environment

    ```sh
    # Unix System
    source venv/bin/activate

    # Windows System
    source venv/Scripts/activate
    ```
18. Install `pip` and `pip-tools` on the virtual environment

    ```sh
    python -m ensurepip --upgrade && pip install pip-tools
    ```
19. Install the dependencies

    ```sh
    pip-sync requirements-dev.txt
    ```
20. Apply the database migrations

    ```sh
    python manage.py migrate
    ```
21. Install the git hook scripts

    ```sh
    pre-commit install
    ```

22. Start the project

    ```sh
    python manage.py test && python manage.py runserver
    ```
    Open http://localhost:8000/resume/api/v1/ with your browser to see the result.

    Visit the documentation http://localhost:8000/resume/docs/

<p align="right">(<a href="#top">back to top</a>)</p>

## Contribution

If you want to contribute to this project, follow these steps:

1. Fork the project
2. Create a branch for your contribution (git checkout -b feature/AmazingFeature)
3. Make the necessary changes
4. Commit your changes (git commit -m 'Add some amazing feature')
5. Push your branch (git push origin feature/AmazingFeature)
6. Open a Pull Request in this repository

<p align="right">(<a href="#top">back to top</a>)</p>
# ToDo

[![GitHub license](https://img.shields.io/github/license/MrFellox/todo-web?color=blue&label=License&style=for-the-badge)](https://github.com/MrFellox/todo-web)
![Version](https://img.shields.io/badge/Version-1.0.0-red?style=for-the-badge)

A simple webpage that helps you to keep track of your tasks.<br>
_2nd finalist in the Episcopal Science and Technology Fair 2022._

<img src = '.github/docs/static/showcase.png' width = 800>

## Features

<li>Responsive design</li>
<li>Runs on your local network. So you can access this page on any device that is connected to your network.</li>
<li>Simple, miniaturized, and minimalistic</li>

## Getting Started

### Running with Docker Compose

To run the app using Docker, you need to have [Docker](https://www.docker.com/get-started) installed on your machine.

1. **Clone the repository** or download the source code from GitHub.
2. **Set `POSTGRES_HOST` to `db` and `POSTGRES_PORT` to `5432`** on the `.env` file. The rest of the variables can be filled in as you wish.

> [!NOTE]
> This is the default configuration for the Docker Compose setup. If you need to change this make sure to also change the `docker-compose.yml` file accordingly.

### Running from Source

Before starting, make sure you have installed [Python](https://python.org/download) 3.9 or above, and PostgreSQL.

1. [Download](https://github.com/MrFellox/todo-web/archive/refs/heads/main.zip) the source code from GitHub, or clone this respository.

2. **(Recommended)** Install web app dependencies using [Poetry](https://python-poetry.org/docs/).

```shell
$ poetry install
```

3. (Optional) If you don't want to use Poetry, you can install the dependencies manually using pip.

```shell
$ pip install -r requirements.txt
```

4. Refer to `.env.example` to create a `.env` file in the root directory of the project. This file is used to configure the app.

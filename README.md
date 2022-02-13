# ToDo

[![GitHub license](https://img.shields.io/github/license/MrFellox/todo-web?color=blue&label=License&style=for-the-badge)](https://github.com/MrFellox/todo-web)
![Version](https://img.shields.io/badge/Version-1.0.0-red?style=for-the-badge)


A simple webpage that helps you to keep track of your tasks.<br>
Created for Episcopal Science and Technology Fair 2022.

<img src = '.github/docs/static/showcase.png' width = 800>


Para leer las instrucciones en Español, ve [aquí](https://github.com/mrfellox/todo-web/blob/main/README_ES.md).

## Features
<li>Responsive design</li>
<li>Runs on your local network. So you can access this page on any device that is connected to your network.</li>
<li>Simple, miniaturized, and minimalistic</li>


## Getting Started

#### Dependencies

Before starting, make sure you have installed [Python](https://python.org/download) 3.9 or above, and make sure it is added to the PATH. You'll also need [SQLite3](https://www.sqlite.org/index.html)

#### Setup and installation

1. [Download](https://github.com/MrFellox/todo-web/archive/refs/heads/main.zip) the source code from GitHub, or clone this respository with Git.

```shell
git clone https://github.com/MrFellox/todo-web.git
```

3. **(Recommended)** Create a new virtual environment and activate it.

```shell
# Example for Windows

# Create a new virtual environment
python3 -m venv venv

# Activate the virtual environment (you'll need to activate it every time you use this project)
venv\Scripts\activate
```

2. Install all dependencies with pip.

```shell
pip install -r requirements.txt
```

3. Create the database.
```shell
# This command only applies to Windows users, if you are in any other OS, just follow the commands in todo/create_db.sql

db_setup.bat
```

4. Run the Flask dev server.
```shell
python3 start.py
```

You can now access the URL that is shown in the console and now you can use the app.
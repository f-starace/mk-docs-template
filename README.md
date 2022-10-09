# Installation


Note, to run the script in this repository, you need to have a version of Python > 3.10


### Using **Poetry** (recommended)
Check out the [Poetry documentation](https://python-poetry.org/docs/) for more information.

Then run:
```bash
poetry install
```

If you want to remove development dependencies (such as `pytest`, `black`, `mkdocs`, ...) to reduce size in production, you can run:

```bash
poetry install --without dev
```

To run the poetry venv:
```bash
poetry shell
```
To add a package in poetry:    
```bash
poetry add <package_name>
```
You can also add a package as a specified group dependency:
```bash
poetry add --group <group_name> <package_name>
```

To list all dependencies:
```bash
poetry show
```

To list all available commands:
```bash
poetry list
```

Poetry handles your dependencies and merge conflicts for you. It also creates a virtual environment for you.


### Using **pip**

```bash
pip install -r requirements.txt
```


# Accessing the Docs
You can access the docs by using the following command:
```bash
mkdocs serve
```
Docs will be served at `localhost:8000` and automatically updated when you make changes to the docs or in the tracked source files.

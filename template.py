import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s: %(levelname)s: %(message)s]")


format_project_name = lambda project_name: project_name.replace(" ", "_").lower() # you can add your username here as per python guidelines @https://packaging.python.org/en/latest/tutorials/packaging-projects/

while True:
    project_name = input("Enter the Project Name: ")
    if project_name != "":
        logging.info(f"Create project by name: {project_name}")
        break

# List of files to be created

filepath_list = [
    "init_setup.sh",  # Basic env setup
    "requirements.txt",  # For installation
    "requirements_dev.txt",  # Requirements.txt for development, experimentation, and testing
    f"src/{format_project_name(project_name)}/__init__.py",  # For source code
    "setup.py",  # For basic setup
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",  # to test in various environments
    f"tests/__init__.py",  # For testing
    f"tests/unit/__init__.py",  # Specfically for unit testing
    f"tests/integration/__init__.py",  # Specifically for integration testing
    ".github/workflows/.gitkeep",  # For github actions
]

if __name__ == "__main__":
    for filepath in filepath_list:
        create_file = False
        filepath = Path(filepath)
        if (not os.path.exists(filepath)):
            dirname, filename = os.path.split(filepath)
            if len(dirname) != 0 and (not os.path.exists(dirname)):
                os.makedirs(dirname, exist_ok=True)
                logging.info("Create director for filepath: {filepath}")
            create_file = True
        elif (os.path.getsize(filepath) == 0):
            create_file = True
        else:
            create_file = False
            logging.info(f"File already exists at: {filepath}")
        if create_file:
            with open(filepath, "w") as f:
                pass
            logging.info(f"Create a new file: {filename} at path: {filepath}")

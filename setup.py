from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # remove newline chars
        requirements = [req.replace("\n", "") for req in requirements]

        # remove the editable install line from install_requires
        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Rhushikesh",
    author_email="rhushikeshsangle9899@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)

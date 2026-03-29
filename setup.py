from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str) -> List[str]:
    """
    Read requirements from a file and return a list of requirements.
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="ml_project",      
    version="0.0.1",
    author="Harshit Tripathi",
    author_email="harshit.tripathi.003@gmail.com",
    description="End to End Machine Learning Project",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")
)
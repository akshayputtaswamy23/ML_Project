from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        requirements = [req.strip() for req in requirements]

        # If '-e .' is in the requirements file, remove it
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Akshay P',
    author_email='akshayputtaswamy23@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)

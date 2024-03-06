from setuptools import setup
from typing import List


#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Yashraj Singh"
DESRCIPTION="This is a first Machine Learning Project"
PACKAGES=["housing"]
REQUIREMENT_FILE_PATH="requirements.txt"

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_PATH) as requirement_file:
        return requirement_file.readlines()

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()
)
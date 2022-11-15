from setuptools import setup,find_packages
from typing import List


# Declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Mangesh Takras"
DESCRIPTION = "This is a first machine learning project of a batch"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"



def get_requirements_list()->List[str]:
    """
    Discription : This function is going to return list of requirement which 
    mentioned in reqirements.txt file

    Return : This function is going to return list which contain name of libraries 
    mentioned in reqirements.txt file  
    """
    with open (REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")
       
setup(
    name=PROJECT_NAME,
    version= VERSION,
    author= AUTHOR,
    description= DESCRIPTION,
    packages= find_packages(),
    install_requires=get_requirements_list()

)
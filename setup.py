import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME="Chicken-Disease-Classification-NN"
AUTHOR_USER_NAME="Shivani6375"
SRC_REPO="chicken_disease_classifier"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description='A chicken disease classification project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    
)
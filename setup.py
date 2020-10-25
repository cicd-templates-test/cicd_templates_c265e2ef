from setuptools import find_packages, setup
from cicd_templates_c265e2ef import __version__

setup(
    name='cicd_templates_c265e2ef',
    packages=find_packages(exclude=['tests', 'tests.*']),
    setup_requires=['wheel'],
    version=__version__,
    description='Databricks Labs CICD Templates Sample Project',
    author=''
)

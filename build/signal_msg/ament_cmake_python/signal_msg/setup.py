from setuptools import find_packages
from setuptools import setup

setup(
    name='signal_msg',
    version='0.0.0',
    packages=find_packages(
        include=('signal_msg', 'signal_msg.*')),
)

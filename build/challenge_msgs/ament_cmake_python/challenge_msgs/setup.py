from setuptools import find_packages
from setuptools import setup

setup(
    name='challenge_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('challenge_msgs', 'challenge_msgs.*')),
)

"""Install file for the bitmask package."""
from setuptools import setup, find_packages


setup(
    name='bitmask',
    version=0.1,
    description='Bitmasks for bulk comparisons',
    author='Alex Hagen',
    author_email='alexhagen6@gmail.com',
    url='https://github.com/alexhagen/bitmask',
    long_description=open('README.md').read(),
    packages=find_packages(),
)

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('./../LICENSE') as f:
    license = f.read()

setup(
    name='RocketSimulator',
    version='0.1.0',
    description='Simulation for Rockets',
    long_description=readme,
    author='OSIM',
    author_email='email@unf.edu',
    url='website.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
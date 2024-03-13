from setuptools import find_packages, setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='PyPublicaties',
    packages=find_packages(include=['PyPublicaties']),
    version='0.1',
    description='A Python library which can be used to interact with the Dutch government\'s publication repository.',
    author='Pascal Venema',
    install_requires=['requests'],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
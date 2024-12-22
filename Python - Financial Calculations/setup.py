# For packaging the project
from setuptools import setup, find_packages

setup(
    name='financial_calculations',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
    ],
    author='Your Name',
    description='A package for financial calculations including cash flows, present/future values, and financial metrics.',
    url='https://github.com/yourusername/financial_calculations_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
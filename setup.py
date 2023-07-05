import os

from setuptools import setup


setup(
    name="hplot",
    version="0.0.2",
    description="Some plot utils for research",
    author="AeroH",
    author_email="zhang.yuh@outlook.com",
    install_requires=[
        "numpy==1.23.1",
        "pytest==7.1.2",
        "matplotlib==3.5.1",
        "pandas==1.4.2",
        "scipy==1.9.0",
        "seaborn==0.11.2",
        "wrapt==1.14.1",
        "tabulate==0.8.10",
        "psutil==5.9.1",
        "tqdm",
    ],
    python_requires=">=3.8",
)

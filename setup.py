import os

from setuptools import setup


setup(
    name="hplot",
    version="0.0.3",
    description="Some plot utils for research",
    author="AeroH",
    author_email="zhang.yuh@outlook.com",
    install_requires=[
        "numpy==1.25.0",
        "pytest==7.4.0",
        "pytest-cov==4.1.0",
        "matplotlib==3.7.2",
        "pandas==2.0.3",
        "scipy==1.11.1",
        "seaborn==0.12.2",
        "wrapt==1.14.1",
        "tabulate==0.9.0",
        "psutil==5.9.1",
        "tqdm",
    ],
    python_requires=">=3.8",
)

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ml_h3n2",
    version="0.0.1",
    author="kianfucius",
    author_email="kian.salamzadeh@hotmail.com",
    description="A small package for predicting the mutation of A/H3N2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kianfucius/ml-h3n2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=['matplotlib']
)

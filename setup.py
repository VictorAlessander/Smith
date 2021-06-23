import io
from setuptools import (
    setup,
    find_packages,
)  # pylint: disable=no-name-in-module,import-error


def dependencies(file):
    with open(file) as f:
        return f.read().splitlines()


with io.open("README.md", encoding="utf-8") as infile:
    long_description = infile.read()

setup(
    name="smith_the_crawler",
    packages=find_packages(exclude=("tests", "examples")),
    version="0.0.12-alpha",
    # license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3.1",
    description="A webscraper with a sofisticated toolkit to scrap the world",
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url="https://github.com/VictorAlessander/Smith/archive/refs/tags/v0.0.12-alpha.tar.gz",
    author="Victor Alessander",
    author_email="victor.alessander.gr@gmail.com",
    url="https://github.com/VictorAlessander/Smith",
    keywords=[
        "crawler",
        "webscraping",
        "webscraper",
        "investments",
        "investment",
        "invest",
    ],
    install_requires=[
        "beautifulsoup4",
        "plotly",
        "requests",
        "pandas",
        "fake-useragent",
        "openpyxl",
    ],
    # install_requires=dependencies('requirements.txt'),
    # tests_require=dependencies("requirements-dev.txt"),
    include_package_data=True,
    # extras_require={"ipython": ["IPython==5.7.0", "ipywidgets==7.1.0",]},
)

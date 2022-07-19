from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="add-markmap",
    version="0.1.0",
    description="Script to generate and append markmap in markdown, for mkdocs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jalmx/add-markmapp-mkdocs",
    author="Xizuth",
    author_email="xizuth@gmail.com",
    license="MIT",
    packages=["addmap"],
    entry_points={'console_scripts':["addmap=addmap.cli:main"]},
    keywords='markmap mkdocs'
)

from setuptools import setup

# https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

with open("Readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="add-markmap-mkdocs",
    version="0.1.0",
    description="Script to generate and append markmap in markdown",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jalmx/add-markmapp-mkdocs",
    author="Xizuth",
    author_email="xizuth@gmail.com",
    license="MIT",
    packages=["mkdocs","markmap","plugin"],
    python_requires=">=3.6",
    zip_safe=False,
)

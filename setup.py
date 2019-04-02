import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fuzzylab",
    version="0.0.11",
    author="Eduardo Avelar",
    author_email="eavelardev@gmail.com",
    description="Python Fuzzy Logic library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ITTcs/fuzzylab",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
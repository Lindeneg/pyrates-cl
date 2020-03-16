import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    fh.close()

with open("requirements.txt", "r") as mFile:
    requirements = mFile.read().split("\n")
    mFile.close()

require = [i for i in requirements if not i == ""]

setuptools.setup(
    name="pyrates-cl",
    version="0.2",
    author="Christian Lindeneg",
    author_email="christian@lindeneg.org",
    description="Currency Conversion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lindeneg/pyrates-cl",
    packages=setuptools.find_packages(),
    install_requires=require,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

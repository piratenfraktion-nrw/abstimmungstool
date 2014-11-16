import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "abstimmungstool",
    version = "0.0.1",
    author = "Gerrit Giehl",
    author_email = "ggiehl@piratenfraktion-nrw.de",
    description = (""
                   ""),
    license = "AGPL",
    keywords = "abstimmungstool",
    url = "https://github.com/piratenfraktion-nrw/abstimmungstool",
    packages=['abstimmungstool', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: AGPL License",
    ],
)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from io import open
from os import path

# read the contents of the README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    author='Martin Isaksson',
    author_email='martin.isaksson@gmail.com',
    name='3gpp-citations',
    version='1.0.0',
    url='https://github.com/martisak/3gpp-citations',
    packages=['standardcitations', ],
    license=open('LICENSE').read(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    scripts=['bin/3gpp-citations'],
    data_files=[
        ('examples', ['examples/3gpp.bib', 'examples/3gpp_38-series.bib'])],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    install_requires=["openpyxl==2.4.8",
                      "bibtexparser==0.6.2",
                      "lxml==3.8.0",
                      "requests==2.21.0",
                      "tqdm==4.29.1"]
)

from distutils.core import setup
from os import path

# read the contents of the README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='3gpp-citations',
    version='0.1dev',
    packages=['3gpp-citations', ],
    license=open('LICENSE').read(),
    long_description=long_description,
    long_description_content_type='text/markdown'
)

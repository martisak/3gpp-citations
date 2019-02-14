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

TESTS_REQUIRE = [
    'pytest==4.2.0',
    'pytest-cov==2.6.1',
    'pytest-flakes==4.0.0',
    'pytest-pep8==1.0.6',
    'pytest-pylint==0.14.',
    'validators==0.12.',
]

setup(
    author='Martin Isaksson',
    author_email='martin.isaksson@gmail.com',
    name='3gpp-citations',
    version='1.1.0',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Natural Language :: English',
    ],
    url='https://github.com/martisak/3gpp-citations',
    packages=['standardcitations', ],
    license=open('LICENSE').read(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    scripts=['bin/3gpp-citations'],
    data_files=[
        ('examples', ['examples/3gpp.bib', 'examples/3gpp_38-series.bib'])],
    setup_requires=["pytest-runner"],
    tests_require=TESTS_REQUIRE,
    install_requires=["openpyxl==2.4.8",
                      "bibtexparser==0.6.2",
                      "lxml==4.3.1",
                      "requests==2.21.0",
                      "tqdm==4.31.1"],
    extras_require={'test': TESTS_REQUIRE},
)

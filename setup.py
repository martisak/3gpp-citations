from setuptools import setup, find_packages

TESTS_REQUIRE = [
    'python-coveralls==2.9.1',
    'coverage==4.5.2',
    'pytest==4.2.0',
    'pytest-cov==2.6.1',
    'pytest-flakes==4.0.0',
    'pytest-pep8==1.0.6',
    'pytest-pylint==0.14.',
    'validators==0.12.',
    'twine==1.12.1'
]

INSTALL_REQUIRE = ["openpyxl==2.4.8",
                   "bibtexparser==0.6.2",
                   "lxml==4.3.1",
                   "requests==2.21.0",
                   "tqdm==4.31.1"]

DESCRIPTION = "This project generates BiBTeX-files for 3GPP specifications."

setup(
    author='Martin Isaksson',
    author_email='martin.isaksson@gmail.com',
    name='3gpp-citations',
    version='1.1.4',
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Topic :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Natural Language :: English',
    ],
    url='https://github.com/martisak/3gpp-citations',
    packages=find_packages(),
    license="MIT",
    scripts=['bin/3gpp-citations'],
    data_files=[
        ('examples', ['examples/3gpp.bib', 'examples/3gpp_38-series.bib'])],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    setup_requires=["pytest-runner"],
    tests_require=TESTS_REQUIRE,
    install_requires=INSTALL_REQUIRE,
    extras_require={'test': TESTS_REQUIRE},
)

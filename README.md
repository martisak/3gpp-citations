# 3GPP Bibtex entry generator

[![Build Status](https://travis-ci.org/martisak/3gpp-citations.svg?branch=master)](https://travis-ci.org/martisak/3gpp-citations) ![](https://img.shields.io/github/issues-raw/martisak/3gpp-citations.svg?style=flat) ![](https://img.shields.io/github/license/martisak/3gpp-citations.svg?style=flat) [![Coverage Status](https://coveralls.io/repos/github/martisak/3gpp-citations/badge.svg?branch=master)](https://coveralls.io/github/martisak/3gpp-citations?branch=master) [![Gitter chat](https://badges.gitter.im/martisak/3gpp-citations.png)](https://gitter.im/3gpp-citations/community "Gitter chat") [![](https://img.shields.io/pypi/v/3gpp-citations.svg?style=flat)](https://test.pypi.org/project/3gpp-citations/)

This project aims to generate [BiBTeX](http://www.bibtex.org/) files that
can be used when citing [3GPP](3gpp.org) specifications. The input is a document list exported from the [3GPP Portal](https://portal.3gpp.org/).

## Installation

Tested with Python 2.7.10.

`pip install 3gpp-citations`

## Instructions

1. Go to the [3GPP Portal](https://portal.3gpp.org/#55936-specifications)
2. Generate the list of specifications you want.
3. Download to Excel and save file
4. Run `python 3gpp-citations.py -i exported.xlsx -o 3gpp.bib`
5. Use in LaTeX.

*Optionally* use the provided `3gpp.bib` directly.

## Things to note

* The output `bibtex` class is set to `@techreport`.
* If you add the option `--xelatex`, break-symbols `\-` will be used in url-fields.
* The version and date are read from 3gpp.org, but it is slow so it takes a while to parse the list. If you find an easy solution to this, let me know.

## Example output

~~~
@techreport{3gpp.36.331,
 author = {3GPP},
 day = {20},
 institution = {{3rd Generation Partnership Project (3GPP)}},
 month = {04},
 note = {Version 14.2.2},
 number = {36.331},
 title = {{Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Resource Control (RRC); Protocol specification}},
 type = {Technical Specification (TS)},
 url = {https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=2440},
 year = {2017}
}
~~~

## Contribute

See our [contribution guidelines](CONTRIBUTING.md).

## Acknowledgment

This project has been updated as part of the [WASP Software and Cloud Technology](http://wasp-sweden.org/graduate-school/courses/software-and-cloud-technology-spring-2019/) course.

This work was partially supported by the Wallenberg AI, Autonomous Systems and Software Program (WASP) funded by the Knut and Alice Wallenberg Foundation.

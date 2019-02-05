# 3GPP Bibtex entry generator

![](https://img.shields.io/github/issues-raw/martisak/3gpp-citations.svg?style=flat)

## Instructions

1. Go to the [3GPP Portal](https://portal.3gpp.org/#55936-specifications)
2. Generate the list of specifications you want.
3. Download to Excel and save file
4. Run `python 3gpp-citations.py -i exported.xlsx -o 3gpp.bib`
5. Use in LaTeX.

*Optionally* use the provided `3gpp.bib` directly.

## Things to note

* The output `bibtex` class is set to `@techreport`.
* If you add the option `--xelatex`, no break-symbols `\-` will be used.
* The version and date are read from the URL, but it is slow so it takes a while to parse the list. If you find an easy solution to this, let me know.

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


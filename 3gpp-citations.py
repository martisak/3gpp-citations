from openpyxl import load_workbook
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import time
import sys

# @Techreport{3gpp.36.331,
#   author = "3GPP",
#   title = "{Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Resource Control (RRC); Protocol specification}",
#   type = "TS",
#   institution = "{3rd Generation Partnership Project (3GPP)}",
#   number = "{36.331}",
#   days = 11,
#   month = jul,
#   year = 2016,
#   url = "http://www.3gpp.org/dynareport/36331.htm",
# }

db = BibDatabase()
db.entries = []

wb2 = load_workbook(sys.argv[1])
sheetnames = wb2.get_sheet_names()
ws = wb2[sheetnames[0]]


for row in ws.iter_rows(row_offset=1):

    number = row[0].value
    title = row[2].value
    type = row[1].value

    if number is None:
        continue

    entry = {
        'ID': "3gpp.{}".format(number),
        'ENTRYTYPE': "techreport",
        'title': "{{{}}}".format(title),
        'type': type,
        'author': "3GPP",
        'institution': "{3rd Generation Partnership Project (3GPP)}",
        'number': number,
        'days': time.strftime("%d"),
        'month': time.strftime("%m"),
        'year': time.strftime("%Y"),
    }

    if row[0].hyperlink is not None:
        entry['url'] = row[0].hyperlink.target

    db.entries.append(entry)


writer = BibTexWriter()
with open(sys.argv[2], 'w') as bibfile:
    bibfile.write(writer.write(db))

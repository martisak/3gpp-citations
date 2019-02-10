"""
This test module contains basic tests for the get_entry function
in standardcitations.
"""

from standardcitations import standardcitations


def test_get_entry_xelatex():
    """
    Test the get_entry function by reading the `test_input.xlsx` workbook
    reading the first (real) row, and producing an entry.
    """

    ws = standardcitations.get_workbook(
        "standardcitations/test/test_input.xlsx")

    row = ws.__getitem__('2')
    entry = standardcitations.get_entry(row, True)

    assert entry['number'] == "36.101"
    assert entry['ID'] == '3gpp.{}'.format(entry['number'])
    assert entry['ENTRYTYPE'] == 'techreport'

"""
This test module contains basic tests for the parse_row function
in standardcitations.
"""

from standardcitations import standardcitations


def test_excel_parse_row():
    """
    Test the parse row function by reading the `test_input.xlsx` workbook
    and reading the first (real) row.
    """

    ws = standardcitations.get_workbook(
        "standardcitations/test/test_input.xlsx")

    number, title, doctype = standardcitations.parse_excel_row(
        ws.__getitem__('2'))

    assert number == u'36.101'
    assert title == u'Evolved Universal Terrestrial Radio Access ' \
        '(E-UTRA); User Equipment (UE) radio transmission and reception'
    assert doctype == u'Technical Specification (TS)'

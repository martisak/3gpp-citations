"""
This test module contains basic tests for the get_worksheet function
in standardcitations.
"""

from standardcitations import standardcitations


def test_get_worksheet():
    """
    Open workbook, return the first sheet and check that is has the correct
    name from the test input file.
    """

    worksheet = standardcitations.get_worksheet(
        "standardcitations/test/test_input.xlsx")
    assert worksheet.title == u'Specifications'

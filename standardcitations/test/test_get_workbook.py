"""
This test module contains basic tests for the get_workbook function
in standardcitations.
"""

from standardcitations import standardcitations


def test_get_workbook():
    """
    Open workbook, return the first sheet and check that is has the correct
    name from the test input file.
    """

    ws = standardcitations.get_workbook(
        "standardcitations/test/test_input.xlsx")
    assert ws.title == u'Specifications'

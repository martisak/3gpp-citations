"""
This test module contains basic tests for the parse_date function
in standardcitations.
"""

from standardcitations import standardcitations


def test_parse_date():
    """
    Check that the date is parsed correctly, and that the output types
    are string.
    """

    year, month, day = standardcitations.parse_date("1982-06-23")

    assert year == "1982"
    assert day == "23"
    assert month == "6"

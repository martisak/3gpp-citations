"""
This test module contains basic tests for the get_entry function
in standardcitations.
"""

import pytest
import validators
from standardcitations import standardcitations


def setup_module():
    """ setup any state specific to the execution of the given module."""

    pytest.ws = standardcitations.get_worksheet(
        "standardcitations/test/test_input.xlsx")


def test_get_entry_required_fields():
    """
    This test repeats the test from format_entry so that
    we can be sure we didn't alter them here.
    """

    row = pytest.ws.__getitem__('2')
    entry = standardcitations.get_entry(row, True)

    # Required fields in @techreport
    assert "year" in entry
    assert "institution" in entry
    assert "title" in entry
    assert "author" in entry


def test_get_entry_xelatex():
    """
    Test the get_entry function by reading the `test_input.xlsx` workbook
    reading the first (real) row, and producing an entry. We don't test
    dynamic fields such as date or note (release) exactly since these are prone
    to change, but rather that they are within expected ranges.
    """

    row = pytest.ws.__getitem__('2')
    entry = standardcitations.get_entry(row, True)

    assert entry['number'] == "36.101"
    assert entry['ID'] == '3gpp.{}'.format(entry['number'])
    assert entry['ENTRYTYPE'] == 'techreport'

    assert validators.between(int(entry['year']), min=2010)
    assert validators.between(int(entry['month']), min=1, max=12)
    assert validators.between(int(entry['day']), min=1, max=31)


def test_get_entry_empty():
    """
    Test the get_entry function by reading the `test_input.xlsx` workbook
    reading the and empty row and check that the output is None
    """

    row = pytest.ws.__getitem__('5')
    entry = standardcitations.get_entry(row, True)

    assert not entry

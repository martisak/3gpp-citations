"""
This test module contains basic tests for the format_entry function
in standardcitations.
"""

import pytest
from standardcitations import standardcitations


def setup_module(module):
    """ setup any state specific to the execution of the given module."""

    pytest.input = {
        "number": "36.100",
        "title": "Some specification",
        "doctype": "Technical Specification (TS)",
        "url": "http://www.3gpp.org"
    }

    pytest.entry = standardcitations.format_entry(**pytest.input)


def test_format_entry_type():
    """
    Check that the output type is a dict.
    """

    assert type(pytest.entry) == dict


def test_format_entry_keys():
    """
    Check that the entry contains all relevant keys
    """

    assert 'ID' in pytest.entry
    assert 'ENTRYTYPE' in pytest.entry
    assert 'title' in pytest.entry
    assert 'type' in pytest.entry
    assert 'author' in pytest.entry
    assert 'institution' in pytest.entry
    assert 'number' in pytest.entry
    assert 'url' in pytest.entry


def test_format_entry_entrytype():
    """
    Check that the entry is of type "techreport"
    """

    assert pytest.entry.get("ENTRYTYPE", None) == "techreport"


def test_format_entry_fields():
    """
    Check that the output contains the input information in the correct
    place.
    """

    # These fields are set in the test, but in case there's a fault
    # there, these should be set to None
    number = pytest.input.get("number", None)
    title = pytest.input.get("title", None)
    doctype = pytest.input.get("doctype", None)
    url = pytest.input.get("url", None)

    # Now assert that they are not None
    assert number
    assert title
    assert doctype
    assert url

    # Compare output to expected output
    assert pytest.entry.get("ID", None) == "3gpp.{}".format(number)
    assert pytest.entry.get("title", None) == "{{{}}}".format(title)
    assert pytest.entry.get("type", None) == doctype
    assert pytest.entry.get("number", None) == number
    assert pytest.entry.get("url", None) == url

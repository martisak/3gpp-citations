"""
This test module contains basic tests for the format_url function
in standardcitations.
"""

from standardcitations import standardcitations


def test_format_url():
    """
    This function tests the default `format_url` function
    """

    url = standardcitations.format_url("36.331")
    assert "\-" in url


def test_format_url_xelatex():
    """
    This function tests the  `format_url` function with xelatex flag.
    """

    url = standardcitations.format_url("36.331", True)
    assert "\-" in url


def test_format_url_no_xelatex():
    """
    This function tests the  `format_url` function with the xelatex flag
    set to False.
    """
    url = standardcitations.format_url("36.331", False)
    assert "\-" not in url

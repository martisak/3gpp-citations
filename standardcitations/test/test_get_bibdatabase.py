"""
This test module contains basic tests for the get_bibdatabase function
in standardcitations.
"""

from bibtexparser.bibdatabase import BibDatabase
from standardcitations import standardcitations


def test_get_bibdatabase():
    """
    Test that the returned database is of the correct type
    and is empty.
    """

    database = standardcitations.get_bibdatabase()

    assert type(database) == BibDatabase
    assert not database.get_entry_list()

"""
This test module contains basic tests for the format_entry function
in standardcitations.
"""

from standardcitations import standardcitations


def test_write_bibtex_empty_stdout(capsys):
    """
    Test function that prints to stdout (without entries). If there are
    no entries, we should get no output either.
    """

    database = standardcitations.get_bibdatabase()
    standardcitations.write_bibtex(database)

    captured = capsys.readouterr()
    assert captured.out == "\n"


def test_write_bibtex_stdout(capsys):
    """
    Test function that prints to stdout (with single entry). We test
    here that with one input we get one output of the correct type.
    (The correctness of the entire output is verified elsewhere.)
    """

    database = standardcitations.get_bibdatabase()

    ws = standardcitations.get_workbook(
        "standardcitations/test/test_input.xlsx")

    row = ws.__getitem__('2')
    entry = standardcitations.get_entry(row, True)

    database.entries.append(entry)
    standardcitations.write_bibtex(database)

    captured = capsys.readouterr()
    assert captured.out.startswith("@techreport")


def test_write_bibtex_file(tmp_path):
    """
    Test function that prints to file. If we specify output to be a file
    we want to make sure we get some output in this file. (The correctness
    of the entire output is verified elsewhere.)
    """

    database = standardcitations.get_bibdatabase()

    ws = standardcitations.get_workbook(
        "standardcitations/test/test_input.xlsx")

    row = ws.__getitem__('2')
    entry = standardcitations.get_entry(row, True)

    database.entries.append(entry)

    directory = tmp_path / "sub"
    directory.mkdir()
    filename = directory / "hello.txt"

    standardcitations.write_bibtex(database, filename=str(filename))

    assert filename.read_text().startswith("@techreport")

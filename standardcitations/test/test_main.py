"""
This test module contains basic tests for the get_entry function
in standardcitations.
"""

from standardcitations import standardcitations


def test_main(tmp_path):
    """
    Test the main function. This mainly tests the chain of events in a context,
    and that the  file written is as expected - complete and correct.

    The input file contains three rows of documents.
    """

    input_filename = "standardcitations/test/test_input.xlsx"

    directory = tmp_path / "sub"
    directory.mkdir()
    output_file = directory / "test_main.bib"
    output_filename = str(output_file)

    args = standardcitations.parse_args(
        ['-o', output_filename, '-i', input_filename])

    standardcitations.main(args)

    file_contents = output_file.read_text()

    assert file_contents.startswith("@techreport")
    assert file_contents.count("@techreport") == 3

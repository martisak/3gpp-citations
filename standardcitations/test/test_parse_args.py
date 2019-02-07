"""
This test module contains basic tests for the parse_args function
in standardcitations.
"""

from standardcitations import standardcitations


def test_parser_input():
    """
    Assert that the input filename is read correctly, and that the XeLaTeX
    flag is not set.
    """

    inputfile = 'inputfile'
    args = standardcitations.parse_args(['-i', inputfile])
    assert args.input == inputfile
    assert not args.xelatex


def test_parser_xelatex():
    """
    Assert that the input filename is read correctly, and that the XeLaTeX
    flag is set when using the '--xelatex' flag.
    """

    inputfile = 'inputfile'
    args = standardcitations.parse_args(['-i', inputfile, '--xelatex'])
    assert args.input == inputfile
    assert args.xelatex


def test_parser_output():
    """
    Assert that the input and output filenames are read correctly,
    and that the XeLaTeX flag is not set.
    """

    inputfile = 'inputfile'
    outputfile = 'outputfile'
    args = standardcitations.parse_args(['-i', inputfile, '-o', outputfile])
    assert args.input == inputfile
    assert args.output == outputfile
    assert not args.xelatex

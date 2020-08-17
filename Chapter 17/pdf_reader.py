import argparse
import subprocess

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument


def argument_parser():
    """Allow user to specify what output from the PDF file is desired."""
    parser = argparse.ArgumentParser(description="PDF file data retrieval")
    parser.add_argument("file", type=argparse.FileType("r"), help="Location of the PDF file")
    parser.add_argument("-t", "--text", action="store_true", help="Dump the text of the PDF")
    parser.add_argument("-m", "--metadata", action="store_true", help="Extract the metadata from the file")

    var_args = vars(parser.parse_args())  # Convert argument namespace to dictionary

    return var_args


def dump_text(file_path):
    """Dump the plain text of the PDF file"""
    text = subprocess.run(["pdf2txt.py", file_path])

    return text


def dump_metadata(file_path):
    """Dump the metadata from the PDF file"""
    with open(file_path, "rb") as pdf:
        parser = PDFParser(pdf)
        metadata = PDFDocument(parser)

        return metadata


if __name__ == "__main__":
    user_args = argument_parser()
    pdf_file = user_args["file"]  # Returned as _io.TextIOWrapper
    text_dump = user_args["text"]
    meta_dump = user_args["metadata"]

    if text_dump:
        print(dump_text(pdf_file.name))
    elif meta_dump:
        print(dump_metadata(pdf_file.name).info)
    else:
        raise ValueError("You need to provide an operation argument.")

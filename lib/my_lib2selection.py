from .my_utils import read_citekeys
import os
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bparser import BibTexParser


def filter_bibtex_entries(bibfile, citekeys):
    """
    Filter BibTeX entries based on provided citation keys.

    Parameters:
        bibfile (str): The path to the BibTeX file.
        citekeys (list): A list of citation keys to filter by.

    Returns:
        list: A list of filtered BibTeX entries that match the provided citation keys.
    """
    with open(bibfile, "r") as bibtex_file:
        parser = BibTexParser(common_strings=True)
        bib_database = bibtexparser.load(bibtex_file, parser=parser)

    selected_entries = [
        entry for entry in bib_database.entries if entry["ID"] in citekeys
    ]
    return selected_entries


def write_bibtex_file(entries, output_file):
    """
    Write selected BibTeX entries to a new file.

    Parameters:
        entries (list): A list of BibTeX entries to write to the file.
        output_file (str): The path to the output BibTeX file.

    Raises:
        IOError: An error occurred writing to the file.
    """
    writer = BibTexWriter()
    db = bibtexparser.bibdatabase.BibDatabase()
    db.entries = entries
    with open(output_file, "w") as bibtex_file:
        bibtex_file.write(writer.write(db))


def main():
    """
    Main function to process citation keys and BibTeX entries.

    Checks the current working directory and processes citation keys from a CSV file.
    Filters BibTeX entries from 'MyLibrary.bib' and writes the selected entries to 'MySelection.bib'.
    """
    expected_directory = "/Users/admin/Projects/literature/yr2_slr/lib"
    current_directory = os.getcwd()

    # Check if the current working directory is as expected
    if current_directory != expected_directory:
        print(
            f"Error: Script is not running in the expected directory. Current directory is {current_directory}"
        )
        return

    # Read citekeys from the file
    citekeys = read_citekeys("../bib/citekeys.csv")
    entries = filter_bibtex_entries("../bib/MyLibrary.bib", citekeys)
    write_bibtex_file(entries, "../bib/MySelection.bib")

    print("BibTeX selection has been written to MySelection.bib")


if __name__ == "__main__":
    main()

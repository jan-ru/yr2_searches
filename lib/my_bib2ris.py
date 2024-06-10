#!/usr/bin/env python3
# import sys
# import os

# CHECK: https://marcel.bollmann.me/blog/turning-bibtex-into-bibliographies-with-python/

from pybtex.database.input import bibtex

item_type = {
    "article": "JOUR",
    "inpress": "INPR",
    "book": "BOOK",
    "misc": "ELEC",
    "inproceedings": "PROC",
    "incollection": "COLL",
    "phdthesis": "PHDT",
}

keys = {
    "year": "PY",
    "url": "UR",
    "number": "M1",
    "title": "TI",
    "eprint": "ID",  # from arXiv
    "volume": "VL",
    "doi": "DO",
    "publisher": "PB",
    "journal": "JO",
    "start_page": "SP",
    "end_page": "EP",
    "address": "PP",
    "note": "N1",
    "month": "DA",
    "timestamp": "DA",
    "biburl": "DP",
    "bibsource": "DS",
    "booktitle": "T1",
    "series": "M1",
    "school": "PB",
    "urn": "C1",
    "archiveprefix": "M3",  # from arXiv
    "primaryclass": "KW",  # from arXiv
    "abstract": "AB",  # from arXiv
    "file": "L1",  # from arXiv
}

# Path to the bibtex file
# bib_file = sys.argv[1]
file = "../ris_files/arxiv"
# Create a parser
parser = bibtex.Parser()
# Load the bibtex file
data = parser.parse_file(file + ".bib")

# Create a dictionary holding all the entries
library = {}
for label, entry in data.entries.items():
    item = {}
    item["type"] = entry.type
    authors = []
    print("\n\n\nentry 1", entry.persons["Author"])
    if len(entry.persons):
        for person in entry.persons.items():  # [0][1]
            print(entry.persons.items())
            print("person: ", person)
            print("len(person) ", len(person))
            print("person[1][0]: ", person[1][0])
            # first_name = " ".join(person.first_names)
            # last_name = " ".join(person.last_names)
            # authors.append(", ".join([last_name, first_name]))
            last_name_first_name = str(person[1][0])
            authors.append(", ".join([last_name_first_name]))
        item["authors"] = authors
        print(item["authors"])
    item["data"] = {}
    for key, content in entry.fields.items():
        if key == "pages":
            pages = content.split("--")
            if len(pages) > 1:
                item["data"]["start_page"], item["data"]["end_page"] = pages
            else:
                item["data"]["start_page"] = pages[0]
        else:
            item["data"][key] = content
    library[label] = item

# Convert the library with bibtex data to ris
ris = ""
for key, item in library.items():
    entry = ""
    type_ = item_type[item["type"]]
    entry += f"TY  - {type_}\n"
    if "authors" in item:
        for author in item["authors"]:
            entry += f"AU  - {author}\n"
    for chunk, data in item["data"].items():
        temp = keys[chunk.lower()]
        entry += f"{temp}  - {data}\n"
    entry += "ER  -\n"
    ris += entry

# Save to file
new_name = f"{file}.ris"
with open(new_name, "w") as f:
    f.writelines(ris)
print("All done")

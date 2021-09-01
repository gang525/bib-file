# --- Python 3.8 ---
"""
@File    :   bibParser.py
@Time    :   2021/03/23
@Author  :   Galen Ng
@Desc    :   Use this to clean up a bib file from Mendeley
"""

# ==============================================================================
# Standard Python modules
# ==============================================================================
import os
import sys
import copy

# ==============================================================================
# External Python modules
# ==============================================================================
import bibtexparser
import re  # for searching strings better

# ==============================================================================
# Extension modules
# ==============================================================================

# --- Use this command in the terminal to get it to work ---
# python bibParser.py <mendeley_autogen_file>.bib <name_you_want>.bib

#  Read input arguments
if len(sys.argv) != 3:
    print("Usage: {sys.argv[0]} INPUT_FILENAME OUTPUT_FILENAME")
    sys.exit()

input_fname = sys.argv[1]
output_fname = sys.argv[2]

# Custom parser to avoid throwing errors on instances such as month = apr
parser = bibtexparser.bparser.BibTexParser(common_strings=True)

with open(sys.argv[1], "r") as input_bib:
    input_data = input_bib.read()

# Temp bib for reformatting bib file
months = [
    (" January,", " {January},"),
    (" February,", " {February},"),
    (" March,", " {March},"),
    (" April,", " {April},"),
    (" May,", " {May},"),
    (" June,", " {June},"),
    (" July,", " {July},"),
    (" August,", " {August},"),
    (" September,", " {September},"),
    (" October,", " {October},"),
    (" November,", " {November},"),
    (" December,", " {December},"),
]

for month in months:
    input_data = input_data.replace(month[0], month[1])

with open("temp.bib", "w") as temp:
    temp.write(input_data)

with open("temp.bib", "r") as temp:
    input_database = bibtexparser.load(temp, parser=parser)

# Sort out relevant entries
new_database_entries = []
for entry in input_database.entries:
    # Go through keys to delete undesired keys
    keys = []
    for key in entry.keys():
        if (
            key == "annote"
            or key == "local-url"
            or key == "mendeley-tags"
            or key == "abstract"
            or key == "file"
            or re.search("date.+", key)
        ):
            keys.append(key)
    for x in keys:
        del entry[x]
    new_database_entries.append(entry)

# Rewrite database
input_database.entries = new_database_entries

with open(sys.argv[2], "w") as output_bib:
    bibtexparser.dump(input_database, output_bib)

# Delete temp
os.remove("temp.bib")

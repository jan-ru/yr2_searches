import glob
import rispy
import pandas as pd

# Fetch all .ris files in the current directory
files = glob.glob("../ris_files/*.ris")
consolidated_data = []

for file in files:
    with open(file, errors="ignore") as bibliography_file:
        entries = rispy.load(bibliography_file)
        for entry in entries:
            # print(entry["authors"][0])
            print(entry)

        # Filter out entries with 'unknown_tag'
        # filtered_entries = [entry for entry in entries
        #                     if 'unknown_tag' not in entry]

        # Convert filtered entries to DataFrame and append to list
        # consolidated_data.append(pd.DataFrame(filtered_entries))
        consolidated_data.append(pd.DataFrame(entries))

# Concatenate all individual DataFrames to get the final DataFrame
result_set = pd.concat(consolidated_data, ignore_index=True)
result_set.to_excel("../ris_files/result_set.xlsx")

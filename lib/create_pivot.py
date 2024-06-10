# from IPython.display import Markdown
from lib.my_excel_lib import get_tables
from lib.my_custom_lib import xls2md

# import numpy as np  # If you need to handle missing values with np.nan

# Initialisatie
input_dir = "tables/"
input_file = "slr_logbook"
input_type = ".xlsx"
input = input_dir + input_file + input_type
output_dir = "./"
output_file = input_file
output_type = ".md"
output = output_dir + output_file + output_type

# Data from excel table
tables = get_tables(input)
df = xls2md(tables["ResultSet1"])

# Create the pivot table (adjust as needed)
pivot_table = df.pivot_table(
    index=["Date", "QueryNr"],
    columns="Database",
    values="Quantity",
    aggfunc="sum",
    margins=True,
    margins_name="Totals",
)

# Convert the pivot table to Markdown format
markdown_table = pivot_table.to_markdown()

# Save the Markdown table to a file
with open(output, "w") as f:
    f.write(markdown_table)

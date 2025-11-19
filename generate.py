# SPDX-License-Identifier: CERN-OHL-P-2.0

import json
import glob
import pandas as pd

# Set the directory where the JSON files are stored
json_dir        = './components/'
footprint_dir   = "./footprints/"
library_path    = "./symbols/"

# Initialize an empty list to store the data from the JSON files
data = []

# Stats
amount_of_components = 0

print("Starting script...")

# Iterate through all the JSON files in the directory
for file in glob.glob(json_dir + '/*.json'):
    # Open the file
    with open(file, 'r') as f:
        # Load the data from the file
        file_data = json.load(f)
        file_data["Library Path"] = library_path + file_data["Library Path"]
        file_data["Footprint Path"] = footprint_dir + file_data["Footprint Path"]
        # Add the data to the list
        data.append(file_data)
        amount_of_components = amount_of_components + 1

# Open a new file to write the combined data to
with open('fw-altium-lib.json', 'w') as outfile:
    # Write the combined data to the file
    json.dump(data, outfile, indent=4)

# Convert the json to an excel
df = pd.read_json('fw-altium-lib.json')

# Convert the JSON file to an Excel file
df.to_excel('fw_lib_generated.xlsx', index=False)

# Print stats
print("Amount of components in database: "+ str(amount_of_components))
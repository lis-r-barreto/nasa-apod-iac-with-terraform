import json
from extract import data_list

# Save the collected data as a single JSON file
output_file = "../nasa-apod-iac-with-terraform/data/apod_data.json"
with open(output_file, "w") as file:
    json.dump(data_list, file)
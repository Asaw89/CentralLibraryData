import csv
import json

input_csv = "book_sampleset_enriched.csv"
output_json = "book_sampleset_enriched.json"

data = []
columns_to_keep = ["Text#", "Title", "Authors", "Genre", "ISBN", "Pages"]

with open(input_csv, mode="r", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader: 
        filtered_row = {col: row.get(col, "") for col in columns_to_keep}
        data.append(filtered_row)

with open(output_json, mode="w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print(f"JSON file created: {output_json}")
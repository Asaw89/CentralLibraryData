import csv
import re

def clean_csv_file(input_file, output_file):
    print(f"Starting to clean: {input_file}")
    print("-" * 60)

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    print(f"Total lines in file: {len(lines)}")

    header = lines[0].strip()
    print(f"Header: {header}")

    cleaned_rows = []
    current_row = ""

    for i, line in enumerate(lines[1:], start=2):
        line = line.strip()
        if not line: 
            continue 
        if re.match(r'^\d+,Text,', line):
            if current_row:
                cleaned_rows.append(current_row)
            current_row = line
        else: 
            current_row += " " + line
    if current_row:
        cleaned_rows.append(current_row)
    
    print(f"Fixed rows created: {len(cleaned_rows)}")
    print("-" * 60)

    with open(output_file, "w", encoding='utf-8', newline='') as file:
        file.write(header + '\n')
        # write each cleaned row
        for row in cleaned_rows:
            file.write(row + '\n')
    
    print(f" Cleaned CSV saved to: {output_file}")
    print("You can now open it in Excel/Numbers")
    print("-" * 60)

    # show a sample of the first 3 cleaned rows
    print("Sample of cleaned data (first 3 books):")
    for i, row in enumerate(cleaned_rows[:3], start=1):
        #show first 100 characters of each row
        preview = row[:100] + "..." if len(row) > 100 else row
        print(f"{i} . {preview}")

    #run the cleaning process
if __name__ == "__main__":
        #change these filenames to match your files
    input_csv = "pg_catalog.csv"
    output_csv = "pg_catalog_cleaned.csv"

    try: 
        clean_csv_file(input_csv, output_csv)
        print("\n Success!")
        print(f"Open '{output_csv}' in Excel/Numbers now!")
    except FileNotFoundError:
        print(f"ERROR: Could not find '{input_csv}'")
        print("Make sure the file is in the same folder as this script!")
    except Exception as e:
        print(f"Error: something went wrong: {e}")
        




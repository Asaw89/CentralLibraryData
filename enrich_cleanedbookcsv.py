import re
import csv
import json

#clean author names by removing birth/death dates
def clean_author_name(author_string):
  authors = author_string.split(';')
  clean_authors = []

  for author in authors:
    parts = author.split(',')
    clean_author = ""
    if len(parts) == 1:
      clean_author = parts[0]
    else:
        if (parts[-1].strip())[0].isdigit():
            clean_author = ",".join(parts[:-1])
        else: 
            clean_author = ",".join(parts)
    clean_author = clean_author.strip()
    clean_authors.append(clean_author)

  return clean_authors 

def clean_bookshelves(bookshelf_string):
   cleaned = bookshelf_string.replace("Browsing: ", "")
   return cleaned
    

if __name__ == "__main__":
    # Read the original CSV and write cleaned version
    with open('pg_catalog_cleaned1.csv', 'r', encoding='utf-8') as input_file, \
         open('pg_catalog_authors_cleaned.csv', 'w', encoding='utf-8', newline='') as output_file, \
         open('pg_catalog_authors_cleaned.json', mode="w", encoding="utf-8") as json_file:
        
        reader = csv.DictReader(input_file)
        # Only use fieldnames with actual names
        fieldnames = ['Text#','Issued','Title','Authors','Bookshelves']
        print(f"{fieldnames}")
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        
        # Write the header
        writer.writeheader()
        
        # Process each row
        count = 0
        data = []
        for dirty_row in reader:

            # elminiate any columns with no column names
            row = {k: v for k, v in dirty_row.items() if k in fieldnames}
            data.append(row)

            # Clean the authors column
            cleaned_authors = clean_author_name(row['Authors'])
            row['Authors'] = cleaned_authors
            
            # Clean the bookshelves column
            cleaned_bookshelves = clean_bookshelves(row['Bookshelves'])
            row['Bookshelves'] = cleaned_bookshelves
            
            writer.writerow(row)
            count += 1
        
        json.dump(data, json_file, indent=4, ensure_ascii=False)

        print(f"Done! Processed {count} books")
        print("Cleaned file saved as 'pg_catalog_authors_cleaned.csv'")
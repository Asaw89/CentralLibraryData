import csv
import json
import random

input_csv_file = "pg_catalog_authors_cleaned.csv"
output_json_file = "pg_final_catalog.json"

all_books = []
used_isbns = []

csv_file = open(input_csv_file, 'r', encoding='utf-8')
csv_reader = csv.DictReader(csv_file)

for book in csv_reader:
    while True: 
        isbn = '978'
        for i in range(10):
            random_digit = random.randint(0,9)
            isbn = isbn + str(random_digit)
        if isbn not in used_isbns:
            used_isbns.append(isbn)
            break
    
    book['isbn'] = isbn
    random_pages = random.randint(200, 400)
    book['pages'] = random_pages
    all_books.append(book)

csv_file.close()

print(f"Saving {len(all_books)} books to JSON file...")
json_file = open(output_json_file, 'w', encoding='utf-8')
json.dump(all_books, json_file, indent=2, ensure_ascii=False)
json_file.close()

print("Done")
print(f"Create {len(all_books)} books with unique ISBNs")
print(f"Saved to: {output_json_file}")
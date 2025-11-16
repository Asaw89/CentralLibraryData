import requests
import json
import time 
import csv

#url https://openlibrary.org/search.json

input_csv = "pg_catalog_authors_cleaned.csv"
output_json = "pg_catalog_final1.json"

#reads JSON file into Python 
rows = []
with open("pg_catalog_authors_cleaned.json", mode ="r", encoding="utf-8") as json_file:
    rows = json.load(json_file)

#given a title+author ask Open Library API to bring back ISBN and page count 
def find_book(title, author):
    # prepare query parameters - think filling out a search form" 
    params = {
        "title": title, 
        "author": author,
    }
    #makes an HTTP GET request - "Hey Open Lib here is my search"
    url = f"https://openlibrary.org/search.json?title={title}]&author={author}" 
    response = requests.get(url, params=params, timeout=10) #returns Json text, timeout means give up after 10 secs
    data = response.json() #turns text to pyton dict 
    docs = data.get("docs", [])
    if not docs: 
        return None, None #two none values - no result (isbn, pages)
    doc = docs[0] #1st result as best match 
    # debug statement print("Available keys:", doc.keys())
    isbn = None 
    ia_list = doc.get("ia")
    
    if doc.get("ia"):
        for identifier in doc['ia']:
            if "isbn" in identifier.lower():
                isbn = identifier.replace("isbn_", "")
                break
    # isbn_list = doc.get("isbn")
    # isbn = isbn_list[0] if isbn_list else None 

    print(f"ISBN: {isbn}")

# loop through books & enrich them
row = rows[10]
title = "alices+adventures+in+wonderland"
author = "carroll"
results = find_book(title, author)

print(results)



          
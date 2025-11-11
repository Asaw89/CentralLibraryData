import csv
import json
from collections import defaultdict

data= []

with open('Periodic Samples.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        Periodical = {
            'periodical_id': row['periodical_id'],
            'title': (row['title']),
            'publisher': row['publisher'],
            'issue_count': int(row['issue_count']),
            'Earliest_Publishing_date': (row['Earliest Publishing date']),
            'Issn' : (row['issn'])
        }
        data.append(Periodical)

with open('periodical.json', 'w') as json_file:
    json.dump(data,json_file, indent = 4)

print ("done")
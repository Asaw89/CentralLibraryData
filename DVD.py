import csv
import json
from collections import defaultdict

data= []

with open('DVDs2.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        dvds = {
            'genres': row['genres'],
            'duration': float(row['duration']),
            'title': row['title'],
            'directors': (row['directors'])
        }
        data.append(dvds)

with open('dvds.json', 'w') as json_file:
    json.dump(data,json_file, indent = 4)

print ("done")
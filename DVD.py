import csv
import json
from collections import defaultdict

data= []

with open('Sample.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        dvds = {
            'genre': row['genres'],
            'duration': float(row['Duration']),
            'title': row['title'],
            'vote_average': float(row['vote_average'])
        }
        data.append(dvds)

with open('dvds.json', 'w') as json_file:
    json.dump(data,json_file, indent = 4)

print ("done")
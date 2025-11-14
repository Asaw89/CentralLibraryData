import re
import csv
import json

def clean_director_name(director_string):
    director = director_string.split(',')
    clearn_directors=[]

    for directors in directors:
        


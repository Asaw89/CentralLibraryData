import csv
import json
import random
import datetime

def getRandomIssn() -> str:
    # Generate a random integer between 0 and 9999 (inclusive)
    random_number_int1 = random.randint(0, 9999)
    random_number_int2 = random.randint(0, 9999)

    # Format the integer as a 4-digit string with leading zeros
    random_number_str1 = f"{random_number_int1:04d}"
    random_number_str2 = f"{random_number_int2:04d}"

    return random_number_str1 + '-' + random_number_str2

def generate_past_date_string(max_days_ago=365*100):
    """
    Generates a random date string in the past.

    Args:
        max_days_ago (int): The maximum number of days in the past the date can be.
                            Defaults to 100 years (365 * 100 days).

    Returns:
        str: A randomly generated date string in 'YYYY-MM-DD' format.
    """
    today = datetime.date.today()
    random_days = random.randint(1, max_days_ago)
    past_date = today - datetime.timedelta(days=random_days)
    return past_date.strftime('%Y-%m-%d')

file_path = 'periodical-titles-UPDATED.csv'
output_file = 'periodicals.json'
data = []
issn_list = []

with open(file_path, 'r', newline='') as csvfile:
    dict_reader = csv.DictReader(csvfile)
    for row in dict_reader:
        # Check if the start date is empty, create random date
        if row['start_date'] == '':
            row['start_date'] = generate_past_date_string
        # End start date check

        # Check if the ISSN is empty, create a unique ISSN to enter in.
        # also checks if the random generation was already used, just in case
        if row['issn'] not in issn_list:
            issn_list.append(row['issn'])
        randomIssn = ''
        if row['issn'] == '':
            while randomIssn in issn_list:
                randomIssn = getRandomIssn()
            issn_list.append(randomIssn)
            row['issn'] = randomIssn
        # End ISSN check

        data.append(row)
        # Access data by column name, e.g., print(row['ColumnName'])

print(issn_list)

with open(output_file, mode='w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=4)
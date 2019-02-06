import json
import urllib
import csv
url = "https://data.cityofboston.gov/resource/crime.json"

response = urllib.urlopen(url)
data = json.loads(response.read())

# open a file for writing

csv_data = open('crime.csv', 'w')

# create the csv writer object

csv_writer = csv.writer(csv_data)

count = 0

for emp in data:
 if count == 0:
     header = emp.keys()
 csv_writer.writerow(header)
 count += 1
 csv_writer.writerow(emp.values())

csv_data.close()

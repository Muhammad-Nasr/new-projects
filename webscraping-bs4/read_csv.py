import csv

with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    next(reader)
    for line in reader:
        print(line)
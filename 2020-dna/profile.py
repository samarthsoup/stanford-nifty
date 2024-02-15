import sys
import csv

data = []
with open(sys.argv[1], "r")as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        data.append(line)

sequence = ''
with open(sys.argv[2], "r") as file:
    sequence = file.read()

print(data)
print(sequence)
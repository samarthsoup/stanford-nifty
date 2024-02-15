import sys
import csv
import re

data = []
with open(sys.argv[1], "r")as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        data.append(line)

sequence = ''
with open(sys.argv[2], "r") as file:
    sequence = file.read()

occurrences = [0] * (len(data[0])-1)

for i,_ in enumerate(data[0][1:]):
    pattern = data[0][i+1]
    regex_pattern = f"(?:{pattern})+"
    matches = re.findall(regex_pattern, sequence)
    if matches:
        longest_match = max(matches, key=len)
        occurrences[i] = len(longest_match)//len(pattern)
    else:
        occurrences[i] = 0


for row_idx, row in enumerate(data[1:]):
    match = True
    for col_idx in range(1, len(row)):
        if int(row[col_idx]) != occurrences[col_idx - 1]:
            match = False
            break
    
    if match:
        print(data[row_idx+1][0])




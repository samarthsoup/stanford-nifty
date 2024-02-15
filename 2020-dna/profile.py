import sys
import csv
import re

def read_data(file_path):
    data = []
    with open(file_path, "r")as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            data.append(line)
    return data

def read_sequence(file_path):
    with open(file_path, "r") as file:
        sequence = file.read()
    return sequence

def analyze_dna(data_path, sequence_path):
    data = read_data(data_path)
    sequence = read_sequence(sequence_path)

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

    results = []
    for row_idx, row in enumerate(data[1:]):
        match = True
        for col_idx in range(1, len(row)):
            if int(row[col_idx]) != occurrences[col_idx - 1]:
                match = False
                break
        
        if match:
            results.append(data[row_idx+1][0])
    return results

if __name__ == '__main__':
    result_names = analyze_dna(sys.argv[1], sys.argv[2])
    for name in result_names:
        print(name)

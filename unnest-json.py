import json
# import logging
# import csv
from collections import Counter

input_file_name = '' # input file path
output_file_name = '' # output file path

with open(input_file_name) as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

newList = []

for item in jsonObject:
    if "field_to_unnest" in item: newList.append(item["field_to_unnest"])  


with open(output_file_name, "w") as jsonFile:
    json.dump(newList, jsonFile)
    jsonFile.close()

#coding=utf-8

import csv
import json
import io

#
# # Function to convert a CSV to JSON
# # Takes the file paths as arguments
# def make_json(csvFilePath, jsonFilePath):
#     # create a dictionary
#     data = {}
#
#     # Open a csv reader called DictReader
#     with io.open(csvFilePath) as csvf:
#         csvReader = csv.DictReader(csvf)
#
#         # Convert each row into a dictionary
#         # and add it to data
#         for rows in csvReader:
#             # Assuming a column named 'No' to
#             # be the primary key
#             print rows;
#             key = rows['No']
#             data[key] = rows
#
#         # Open a json writer, and use the json.dumps()
#     # function to dump data
#     with io.open(jsonFilePath, 'w') as jsonf:
#         jsonf.write(json.dumps(data, indent=4))
#
#     # Driver Code
#
#
# # Decide the two file paths according to your
# # computer system
# csvFilePath = 'left.csv'
# jsonFilePath = 'lft.json'
#
# # Call the make_json function
# make_json(csvFilePath, jsonFilePath)


def convertFile(input, output):
    csvfile = open(input, 'r')
    jsonfile = open(output, 'w')

    fieldnames = ("位置","标题","封面图片链接","文章链接","作者头像链接","作者名","文章标签")
    reader = csv.DictReader( csvfile, fieldnames)
    reader.next()
    json_data = []
    for row in reader:
        json_item = {}
        json_item['title'] = row['标题']
        json_item['img_url'] = row['封面图片链接']
        json_item['img_href'] = row['文章链接']
        json_item['author_avatar_url'] = row['作者头像链接']
        json_item['author_name'] = row['作者名']
        json_item['tags'] = row['文章标签']
        json_data.append(json_item)

    json.dump(json_data, jsonfile, indent=2, sort_keys=True)
    jsonfile.write('\n')
    print json.dumps(json_data, indent=2, sort_keys=True),

convertFile('left.csv', 'left.json')
print '\n\n-------------------------------------\n\n'
convertFile('right.csv', 'right.json')
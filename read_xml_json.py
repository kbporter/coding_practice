# coding: utf-8

import json
import csv
import io

filelist = ['world-check']
filepath = './'
filetype = '.json'
# tag = 'person'


def flattenjson(b, delim):
    """ takes json input, and flattns nested keys with naming format:
    key1 + delim + nestedkey2 + ...."""
    val = {}
    if isinstance(b, unicode):
        # for debugging purposes, if receives value instead of key
        print 'unicode content:', b, 'type', type(b), 'len', len(b)
    for i in b.keys():
        if isinstance(b[i], dict):
            # recursively goes through dict items
            get = flattenjson(b[i], delim)
            for j in get.keys():
                val[i + delim + j] = get[j]
        elif isinstance(b[i], list):
            # if the content of a dict is a list of dicts
            if len(b[i]) > 0:
                # check to make sure the value of the key
                # is not an empty list, or a list of one value
                # e.g. 'mykey':[""]
                if isinstance(b[i][0], dict):
                    get = flattenjson(b[i][0], delim)
                    for j in get.keys():
                        val[i + delim + j] = get[j]
                else:
                        # just take the value if list != dict
                        # e.g. val['mykey'] = [""]
                    val[i] = b[i]
            else: 
                val[i] = b[i]
        else:
                val[i] = b[i]  
    return val


for filename in filelist:
    curfile = filepath + filename + filetype
    newfile = filepath + 'flat_' + filename + '.csv'

    print curfile

    with open(curfile, 'r') as json_data:
        d = json.load(json_data)
        json_data.close()
    totalrows = len(d)
    print 'numrows:', totalrows

file_data = open('people.csv', 'w') #, encoding='utf8'
csvwriter = csv.writer(file_data)
i = 0

for count in d['records']['record']:
    flat = flattenjson(count, '_')
    if i == 0:
        header = flat.keys()
        csvwriter.writerow(header)

    i += 1
    liste = {}
    for col in header:
        liste[col]=flat[col]

    csvwriter.writerow(liste.values())

file_data.close()

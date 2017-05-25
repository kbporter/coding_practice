
# coding: utf-8

import json
import csv

filename = 'cs_json_data'
filepath = './'
filetype = '.json'


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

curfile = filepath + filename + filetype
newfile = filepath + 'flat_' + filename + '.csv'

print "infile: ", curfile, '\noutfile: ', newfile


with open(curfile, 'r') as json_data:
    d = json.load(json_data)
    json_data.close()
totalrows = len(d)
print 'numrows:', totalrows

i = 0
flatlist = []
keylist = set()
for count in d:
    flat = flattenjson(count, '_')
    flatlist.append(flat)
    keylist.update(flat.keys())

with open(newfile, 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, keylist)
    w.writeheader()
    w.writerows(flatlist)

f.close()

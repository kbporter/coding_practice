import json
import csv

#filename = 'clusters_test'
filename = 'testjsonnewline'
filepath = './'
filetype = '.json'

curfile = filepath + filename + filetype
newfile = filepath + 'flat_' + filename + '.csv'

print "infile: ", curfile, '\noutfile: ', newfile


with open(curfile, 'r') as json_data:
	dlist = []
	i = 0
	with open(newfile, 'wb') as f:  # Just use 'w' mode in 3.x
		for row in json_data:
			d = json.loads(row)
			if i == 0:
				keylist = d.keys()
				w = csv.DictWriter(f, keylist)
				header = {}
				for n in keylist: 
					header[n] = n
				w.writerow(header)
				i += 1
			w.writerow(d)
f.close()
json_data.close()

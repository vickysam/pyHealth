import csv
data = {}
with open('parent_cat.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
	for row in reader:
		data[row['concept_id']] = row['category_id']

print "Supplied : ", data

with open('snomed_test.csv', 'rb') as csvfile:
	spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
	for row in spamreader:
		if data.has_key(row['parent_id']):
			data[row['chiled_id']] = data[row['parent_id']]

print "Altered : ", data

with open('final_out.csv', 'w') as csvfile:
    fieldnames = ['concept_id', 'category_id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for codes in data:
    	#print codes, data[codes]
    	writer.writerow({'concept_id': codes, 'category_id': data[codes]})
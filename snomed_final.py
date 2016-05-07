import csv
data = []
snomed_data = []
with open('parent_cat_final.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
	for row in reader:
		data.append([row['concept_id'],row['category_id']])

print "Supplied : ", data

with open('snomed_final.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
	for row in reader:
		snomed_data.append([row['id'],row['destinationId'],row['sourceId'],0])

#print "Altered : ", data
print len(data)
print len(snomed_data)

csvfile = open('snomed_final_out.csv', 'w')
writer = csv.DictWriter(csvfile, fieldnames=['id','destinationId','sourceId','category_id'])
writer.writeheader()

i = 0

for parent in data:
	for child in snomed_data:
		if parent[0] == child[2] and child[3] == 0:
			child[3] = parent[1]
			i = i + 1
			writer.writerow({'id': child[0], 'destinationId': child[1], 'sourceId': child[2], 'category_id':child[3]})
			print i, child

print len(data)
print len(snomed_data)


for parent in data:
	for child in snomed_data:
		if parent[0] == child[1] and child[3] == 0:
			child[3] = parent[1]
			data.append([child[2],child[3]])
			i = i + 1
			writer.writerow({'id': child[0], 'destinationId': child[1], 'sourceId': child[2], 'category_id':child[3]})
			print i,child
			if child in snomed_data: snomed_data.remove(child)

print "Completed...."

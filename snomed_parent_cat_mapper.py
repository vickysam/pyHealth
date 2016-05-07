import csv
import pymedtermino
from pymedtermino.snomedct import *
pymedtermino.LANGUAGE = "en"
pymedtermino.REMOVE_SUPPRESSED_CONCEPTS = False

input_delta_file = 'sct2_Concept_Delta_INT_20160131.csv'
output_delta_file = 'sct2_Concept_Delta_INT_20160131_Top_Category_Mapped.csv'

data = []
snomed_data = []

with open('top_parent_cat.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
	for row in reader:
		data.append([row['top_concept_id'],row['top_category_code']])

print "Supplied : ", data

with open(input_delta_file, 'rb') as csvfile:
	reader = csv.DictReader(csvfile, delimiter='	', quotechar='"')
	for row in reader:	
		snomed_data.append([row['id'],row['effectiveTime'],row['active'],row['moduleId'],row['definitionStatusId'],0,0])

csvfile = open(output_delta_file, 'w')
writer = csv.DictWriter(csvfile, fieldnames=['id','effectiveTime','active','moduleId','definitionStatusId','topCategoryCode','topCategoryId'])
writer.writeheader()

i = 0

for concept in snomed_data:
	ancestors = list(SNOMEDCT[concept[0]].ancestors())	
	category = SNOMEDCT[138875005]
	if len(ancestors) >= 2:
		category = ancestors[-2]
		if len(ancestors) >= 3:
			if ancestors[-3].code == '406455002' or ancestors[-3].code == '116273005':
				category = ancestors[-3]
	else:
		category = SNOMEDCT[138875005]

	term = category.term

	for item in data:
		if item[0] == str(category.code):
			term=item[1]

	writer.writerow({'id': str(concept[0]), 'effectiveTime': concept[1],'active': concept[2],'moduleId': str(concept[3]),'definitionStatusId': str(concept[4]) , 'topCategoryCode': term,'topCategoryId': str(category.code)})
	i = i + 1
csvfile.close()
print "Completed...."

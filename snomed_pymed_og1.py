import csv
import pymedtermino
from pymedtermino.snomedct import *

pymedtermino.LANGUAGE = "en"
pymedtermino.REMOVE_SUPPRESSED_CONCEPTS = True

root = 138875005
data = [404684003,71388002,363787002,123037004,410607006,105590001,373873005,123038009,370115009,106237007,78621006,272379006,308916002,48176007,243796009,254291000,260787004,362981000,419891008,]

csvfile = open('snomed_pymed_cat_out1.csv', 'w')
writer = csv.DictWriter(csvfile, fieldnames=['main_parent_id','snomed_id','category'])
writer.writeheader()

i = 0

for child in data:
		concept = SNOMEDCT[child]
		writer.writerow({'main_parent_id': root, 'snomed_id': concept.code , 'category': concept.term})
		i = i + 1
		print "First ", i , root,concept.code,concept.term

for concept in SNOMEDCT.all_concepts_no_double():
	if concept.code not in data and concept.code != root:
		category = list(concept.ancestors())[-2]
		writer.writerow({'main_parent_id': category.code, 'snomed_id': concept.code , 'category': category.term})
		i = i + 1
		print "Last ", i , category.code,concept.code,category.term

print "Completed...."

import csv
import pymedtermino
from pymedtermino.snomedct import *

pymedtermino.LANGUAGE = "en"
pymedtermino.REMOVE_SUPPRESSED_CONCEPTS = True

root = 138875005
data = [404684003,71388002,363787002,123037004,410607006,105590001,373873005,123038009,370115009,106237007,78621006,272379006,308916002,48176007,243796009,254291000,260787004,362981000,419891008,]

csvfile = open('snomed_pymed_cat_out2.csv', 'w')
writer = csv.DictWriter(csvfile, fieldnames=['main_parent_id','snomed_id','description'])
writer.writeheader()

i = 0

#Writing Root
concept = SNOMEDCT[root]
for con in concept.terms:
		writer.writerow({'main_parent_id': 0, 'snomed_id': concept.code , 'description': con.encode("utf8")})
		i = i + 1
		print "First ", 0 , concept.code,con.encode("utf8")

#Writing First Level
for child in data:
		concept = SNOMEDCT[child]
		for con in concept.terms:
			writer.writerow({'main_parent_id': root, 'snomed_id': concept.code , 'description': con.encode("utf8")})
			i = i + 1
			print "First ", i , root,concept.code,con.encode("utf8")

#Writing Tree
for concept in SNOMEDCT.all_concepts_no_double():
	if concept.code not in data and concept.code != root:
		category = list(concept.ancestors())[-2]
		for con in concept.terms:
			writer.writerow({'main_parent_id': category.code, 'snomed_id': concept.code , 'description': con.encode("utf8")})
			i = i + 1
			print "Tree ", i , category.code,concept.code,con.encode("utf8")

print "Completed...."

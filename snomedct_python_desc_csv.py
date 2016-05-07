import sys
import csv
import pymedtermino
pymedtermino.LANGUAGE = "en"
pymedtermino.REMOVE_SUPPRESSED_CONCEPTS = True
from pymedtermino.snomedct import *
codes = [386617003, 225552003, 63901009, 365220004, 249244000, 249236000]
print codes

CSV_FILE = "Snomedct_new.csv"
Headers = ("Code", "Term")
op_file = open(CSV_FILE,"wb")
c = csv.writer(op_file)
c.writerow(Headers)
count = 0
for code in codes:
	print "Code : ", code
	count = 0
	for child in SNOMEDCT[code].descendants():
		c.writerow((child.code,child.term.encode('utf-8').strip()))
		count+=1
	print "Total : ",count
op_file.close()

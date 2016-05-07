import sys
import csv
import pymedtermino
pymedtermino.LANGUAGE = "en"
pymedtermino.REMOVE_SUPPRESSED_CONCEPTS = True
from pymedtermino.snomedct import *
code = sys.argv[1]
print code
CSV_FILE = "Snomedct_"+str(code)+".csv"
Headers = ("Code", "Term")
op_file = open(CSV_FILE,"wb")
c = csv.writer(op_file)
c.writerow(Headers)
for child in SNOMEDCT[code].descendants():
		c.writerow((child.code,child.term.encode('utf-8').strip()))
op_file.close()
import csv
import sys

passdictionary = {}

try:
  myfile = open("/etc/passwd")
except IOError:
  print "The path is not valid"
  sys.exit()

for line in myfile:
  if line.startswith("#"):
    pass
  else:
    splitline=line.split(":")
    key = splitline[0]
    value = splitline[2]
    passdictionary[key]=value

with open('csvfile2.csv', 'w') as f:
  o = csv.writer(f, delimiter='\t')
  for user_name, user_id in passdictionary.iteritems():
    o.writerow([user_name, user_id])
    #o.writerows(passdictionary.iteritems())
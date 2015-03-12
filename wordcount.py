import sys

lineno=0
charno=0
whordno=0
uniquewordno=0
word_set = set()
words = []

path = raw_input("Write input file path: ")

try:
  myfile = open(path)
except IOError:
  print "The path is not valid. Try again..."
  sys.exit()

for line in myfile:
  lineno+=1
  charno+=len(line)
  words = line.split(' ')
  whordno+=len(words)
  for word in words:
    if word in word_set:
      pass
    else:
      word_set.add(word)

print "Number of lines is " + str(lineno)
print "Number of words is " + str(whordno)
print "Number of chars is " + str(charno)
print "Number of unique words is " + str(len(word_set))
print word_set

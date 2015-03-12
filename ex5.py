import sys
#from string import digits


words_list = []
word_dictionary = {}

def get_dictionary(word_list):
  for word in word_list:
    if word in word_dictionary:
      word_dictionary[word]=word_dictionary[word]+1
    else:
      word_dictionary[word] = 1
  return word_dictionary

def get_max(pairs):
  (max_key, maxim) = pairs[0]
  for key, elem in pairs:
    if elem>maxim:
      maxim=elem
      max_key=key
  return max_key, maxim


try:
  myfile = open("filetostrip.txt")
except IOError:
  print "The path is not valid. Try again..."
  sys.exit()

for line in myfile:
  for word in line.split(' '):
    #print word.lower().translate(None, digits)
    stripped_list = ''.join(i for i in word.lower() if i.isalpha())
    words_list.append(stripped_list)


print words_list
print get_dictionary(words_list)
max_max = get_max(word_dictionary.items())
print 'The word with the most occurrences is ' + str(max_max)
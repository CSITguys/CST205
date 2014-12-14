#CST 205 multimedia programming
#Lab 14 word counts and files

#Brian Carlston
#Phillip Powell
#David Klier
#Rahel Tilahun

def greenEggsCount():
  textFile = pickAFile()
  openFile = open(textFile, "rt")
  text = openFile.read()
  tokens = text.split()
  count = len(tokens)
  histogram ={}

  for word in tokens:
    if word.lower() in histogram:
      histogram[word.lower()] += 1
    else:
      histogram[word.lower()] = 1
      
  max = histogram[tokens[0].lower()]
  maxWord =tokens[0].lower()
  for key in histogram:
    if max < histogram[key]:
      max = histogram[key]
      maxWord = key
  printNow( histogram)
  printNow("Total words: " + str(count))
  printNow("Most occuring word: " + maxWord + " - " +str(max) )
  
def newsFeed():
  textFile = pickAFile()
  openFile = open(textFile, "rt")
  text = openFile.read()
  index  = string.find(text, "<h3 class=\"archive_title\"")
  print index
  print text[index:]
    
    
#CST 205 multimedia programming
#Lab 14 word counts and files

#Brian Carlston
#Phillip Powell
#David Klier
#Rahel Tilahun
import string
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
  printNow("*** Otter Realm Breaking News! ****")
  index  = string.find(text, "<h3 class=\"archive_title\"")
  while index != -1:
    entryEndpoint = string.find(text,"</h3>")
    text = text[index:]
    entryEndpoint = string.find(text,"</a>")
    startPoint = string.find(text, "k\">")
  
    entry = text[startPoint+3:entryEndpoint]
 
    entry = string.lstrip(entry)
    entry = string.rstrip(entry)
    entry = entry.replace('&nbsp;'," " )
    entry = entry.replace('&#8230;'," " );
    printNow(">>  " + entry)
    text = text[entryEndpoint:]
    index  = string.find(text, "<h3 class=\"archive_title\"")
 
 
    
    
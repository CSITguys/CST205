inventory =[]
items ={}

def game():
    printNow("*** Welcome to The CSIT Guys? House of Horrors! ***")
    printNow("In each room you will be told which directions you can go.")
    printNow("You'll be able to go north, south, east or west by typing that direction.")
    printNow("Type help to redisplay this introduction.")
    printNow("Type exit to quit at any time.")
    #constants to make code easier to read
    DIRECTION = 0
    ROOM_NAME = 1
    
    userInput = ""
    currentRoom = "porch"
    global inventory
    global items 
    
    items = initializeItems()
    # dictionary of all rooms in the game
    rooms = initializeRooms()
    while userInput!="exit":
        roomDescription(currentRoom)
        #get list of rooms available to travel to from current room
        roomOptions = rooms[currentRoom]
        #loop through all rooms connected to current room
        userInput = requestString("Choose a direction")
        userInput = parse(userInput)
        if len(userInput)>0:            
            if(userInput=="north" or userInput=="south" or userInput== "east" or userInput=="west"):
                validDirection = false
                for i in range(0,len(roomOptions)):
                    #check if userinput direction is valid
                    if userInput == roomOptions[i][DIRECTION]:
                        validDirection = true
                        currentRoom = roomOptions[i][ROOM_NAME]
                if not validDirection:
                    printNow("Direction is unavailable") 
            elif(userInput[:4]=='take'):
                if takeItem(currentRoom,userInput[5:]):
                  printNow(userInput[5:] + " now in inventory")
                else:
                  printNow("cannot pick up item")
            elif(userInput[:4]=='read'): 
                if(userInput[5:]== "nothing"):
                  printNow("cannot read item")  
        else:
            printNow("I don't understand what you are saying")
        printNow("")    
    printNow("goodbye")
    
def initializeRooms():
    porch = [["north","entry way"]]
    entryway = [["north","kitchen"],["south","porch"],["east","living room"]]
    diningroom = [["east","kitchen"]]
    kitchen = [["south","entry way"],["west","dining room"]]
    livingroom = [["north","bathroom"],["west","entry way"],["east","bedroom"]]
    bathroom = [["south","living room"]]
    bedroom = [["west","living room"]]
    rooms = {"kitchen":kitchen, "porch":porch, "entry way":entryway, "dining room":diningroom, "living room":livingroom,"bathroom":bathroom,"bedroom":bedroom}
    return rooms

def initializeItems():
    items = {"knife":"kitchen", "book":"living room"}
    return items
               
def parse(userInput):
    if userInput is not None:
      userInput = userInput.lower()
      userInputTokens = userInput.split()
      #error checking 
      if (userInput == "north" or userInput == "south" or userInput == "east" or userInput == "west"):
          return userInput
      elif (userInput == "help" or userInput == "?" or userInput == "h"):
          displayHelp()
          return "help"
      elif (userInput == "exit"):
          return userInput
      elif (userInput == "inventory" or userInput=="i"):
          displayInventory( inventory)
          return "i"
      elif (userInputTokens[0] == "pickup" or userInputTokens[0] == "pick" or userInputTokens[0] == "take"):
          if len(userInputTokens)<2:
            return "take nothing"
          elif userInputTokens[1]=="up":
            if len(userInputTokens)<3:
              return "take nothing"
            else:
              return "take " + userInputTokens[2]
          else:
            return "take " + userInputTokens[1] 
      elif (userInputTokens[0] == "read"):
          if len(userInputTokens)<2:
            return "read nothing"
          else:
            if readItem(userInput[5:]):
              return "read something"
            else:
              return "read nothing"
      else: 
          return ""
    else:
        return ""
        
def displayHelp():
    printNow("You have choosen to display the Help Menu")
    printNow("")
    printNow("*** Welcome to The CSIT Guys? House of Horrors! ***")
    printNow("In each room you will be told which directions you can go.")
    printNow("You'll be able to go north, south, east or west by typing that direction.")
    printNow("Some rooms will have items that can taken by typing 'take item' ")
    printNow("Type inventory or 'i' to display your inventory")
    printNow("Items in inventory can be read by typing 'read' then the name of the item ie. 'read book'")
    printNow("Type help,h, or ? to redisplay this introduction.")
    printNow("Type exit to quit at any time.")
    userInput = ""
    choice = userInput
    return choice
 
def displayInventory(inventory):
    printNow("Inventory:")
    printNow(inventory) 
       
def roomDescription(room):
    if room == "porch":
        printNow(room.upper())
        printNow("You are on the porch of a haunted house")
        printNow("You can go north (entryway) into the house ... if you dare")
    if room == "entry way":
        printNow(room.upper())
        printNow("You are in the entryway of the house")
        printNow("A grandfather clock chimes loudly as the door closes behind you")
        printNow("You feel a sense of dread")
        printNow("There is a passageway to the north (kitchen), a door to the east (living room), and a door to the west(dining room)")
        printNow("The porch is behind you to the south")
    if room == "dining room":
        printNow(room.upper())
        printNow("You are in the dining room of the house")
        printNow("In the center of the room is the dining room table that has been set, but is completely empty")
        printNow("There is passage to the east(kitchen))")
    if room == "kitchen":
        printNow(room.upper())
        printNow("There is a smell of burnt flesh")
        if "knife" in items: 
          printNow("A butcher knife rests on the counter, with a pig’s wet heart dripping into the sink")
        else:  
          printNow("A pig’s wet heart is dripping into the sink")
        printNow("On the table, a Martha Stewart catalog is sealed with dry blood")
        printNow("A candlelight flickers from a cool breeze")
        printNow("The is a door to the south (entryway) and a passage to the west (dining room)")
    if room == "living room":
        printNow(room.upper())
        printNow("A rocking chair rocks to-and-fro, but no one sits upon it")
        printNow("A mounted bear head seems to follow your every movement")
        if "book" in items:
          printNow("A book is sitting on the end table")
        printNow("The fireplace’s embers indicate it has been used recently")
        printNow("There is a door to the west (entryway), a door to the north (bathroom), and a door to the east (bedroom)")
    if room == "bathroom":
        printNow(room.upper())
        printNow("You are staring at yourself through a water spotted mirror")
        printNow("There is a medicine cabinet to your left. The sink has been used to wash the blood off something")
        printNow("The toilet sits to the right of you and there is no toilet paper")
        printNow("There is only one door to the south(Living Room)")
    if room == "bedroom":
        printNow(room.upper())
        printNow("You walk into a dark and deserted bedroom")  
        printNow("To your right there are weird noises coming from behind a closet door")
        printNow("To your left underneath the bed there is some sort of bloody object")
        printNow("There is only one door to the west(Living Room)")

def takeItem(room, item):
    itemTaken = false
    global inventory 
    if item in items:
      if items[item] == room:
        inventory = inventory + [item]
        itemTaken= true 
        del items[item]   
    return itemTaken
 
def readItem(item): 
    global inventory
    if item in inventory:
      if item == "book":
        printNow("HOW TO SURVIVE A HAUNTED HOUSE")
        printNow("rule #1 don't enter haunted house.")
        printNow("rule #2 don't stop to read anything.")
        printNow("rule #3 stay near the entryway.")
        printNow("rule #4 find a weapon")
        printNow("rule #5 get out of the haunted house!")
      return true
    return false  

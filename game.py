#CST 205 Multimedia Programming
#Lab 12 Adventure game
#Brian Carlston
#David Klier
#Phillip Powell
#Rahel Tilahun


#Global variables for player inventory and interactive items
inventory =[]
items ={}
#Main function runs game
def game():
    #constants to make code easier to read
    DIRECTION = 0
    ROOM_NAME = 1
    
    global inventory
    global items 
    
    userInput = ""
    currentRoom = "porch"
    closetOpened = false
    inventory = []
    items = initializeItems()
    # dictionary of all rooms in the game
    rooms = initializeRooms()

    printNow("*** Welcome to The CSIT Guys\' House of Horrors! ***")
    printNow("To win the game, search for the secret in the house.")
    printNow("In each room you will be told which directions you can go.")
    printNow("You can go north, south, east or west by typing that direction.")
    printNow("Type help to redisplay this introduction.")
    printNow("Type exit to quit at any time.")
    
    

    while userInput!="exit":
        roomDescription(currentRoom)
        #get list of rooms available to travel to from current room
        roomOptions = rooms[currentRoom]
        #loop through all rooms connected to current room
        userInput = requestString("Choose a direction")
        userInput = parse(userInput)
        if len(userInput)>0: 
            if(userInput[:4]=='open'):
                if(userInput[5:]== "nothing" or currentRoom!="bedroom"):
                  printNow("cannot open anything")
                else:
                  userInput = openCloset()  
                  rooms["bedroom"] += [["east","secret room"]]         
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
            if(currentRoom == "secret room"):
                userInput = winGame()
                    
        else:
            printNow("I do not understand what you are saying.")
        printNow("")    
    printNow("Goodbye")
    
#Initialize all the rooms in the game using a graph data structure to travel between rooms\nodes. Store in dictionary.   
def initializeRooms():
    porch = [["north","entryway"]]
    entryway = [["north","kitchen"],["south","porch"],["east","living room"]]
    diningroom = [["east","kitchen"]]
    kitchen = [["south","entryway"],["west","dining room"]]
    livingroom = [["north","bathroom"],["west","entryway"],["east","bedroom"]]
    bathroom = [["south","living room"]]
    bedroom = [["west","living room"]]
    secretroom=[["west","bedroom"]]
    rooms = {"kitchen":kitchen, "porch":porch, "entryway":entryway, "dining room":diningroom, "living room":livingroom,"bathroom":bathroom,"bedroom":bedroom,"secret room":secretroom}
    return rooms

def initializeItems():
    items = {"knife":"kitchen", "book":"living room"}
    return items

#Sanity checks and validates userInput returns modified string of action to take.               
def parse(userInput):
    if userInput is not None and userInput!="" :
      userInput = userInput.lower()
      userInputTokens = userInput.split()
      
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
      elif (userInputTokens[0] == "open"):
          if len(userInputTokens)<2:
              return "open nothing"
          else:
              if(userInput[5:]=="closet"):
                  return "open closet" 
              else:
                  return "open nothing"  
      else: 
          return ""
    else:
        return ""
        
def displayHelp():
    printNow("You have choosen to display the Help Menu")
    printNow("")
    printNow("*** Welcome to The CSIT Guys\' House of Horrors! ***")
    printNow("In each room you will be told which directions you can go.")
    printNow("You can to go north, south, east or west by typing that direction.")
    printNow("Some rooms have items that can taken by typing 'take item'. ")
    printNow("Some rooms have closets that can be opened by typing 'open closet'. ")
    printNow("Type inventory or 'i' to display your inventory.")
    printNow("Items in inventory can be read by typing 'read' then the name of the item e.g. 'read book'. ")
    printNow("Type help, h, or ? to redisplay this introduction.")
    printNow("Type exit to quit at any time.")
 
 
def displayInventory(inventory):
    printNow("Inventory:")
    printNow(inventory) 

#Displays description for each room              
def roomDescription(room):
    if room == "porch":
        printNow(room.upper())
        printNow("You are on the porch of a haunted house.")
        printNow("You can go north (entryway) into the house ... if you dare.")
    if room == "entryway":
        printNow(room.upper())
        printNow("You are in the entryway of the house.")
        printNow("A grandfather clock chimes loudly as the door closes behind you.")
        printNow("You hear distant, shambling footsteps to the east.")
        printNow("There is a passageway to the north (kitchen), and a door to the east (living room).")
        printNow("The porch is behind you to the south (porch).")
    if room == "dining room":
        printNow(room.upper())
        printNow("You are in the dining room of the house.")
        printNow("In the center of the room is a dining room table that has been set, but no one sits.")
        printNow("There is passage to the east (kitchen).")
    if room == "kitchen":
        printNow(room.upper())
        printNow("You are in the kitchen.")
        printNow("There is a smell of burnt flesh.")
        if "knife" in items: 
          printNow("A knife rests on the counter, with a pig\'s wet heart dripping into the sink.")
        else:  
          printNow("A pig\'s wet heart is dripping into the sink.")
        printNow("On the table, a Martha Stewart catalog is sealed shut with dried blood.")
        printNow("A faint candlelight flickers from a cool breeze.")
        printNow("The is a door to the south (entryway) and a passage to the west (dining room)")
    if room == "living room":
        printNow(room.upper())
        printNow("You are in the living room.")
        printNow("A rocking chair rocks to-and-fro, as though it was just bumped heavily.")
        printNow("A mounted bear head seems to follow your every movement.")
        if "book" in items:
          printNow("A book is sitting on the end table.")
        printNow("The fireplace\'s embers indicate it has been used recently.")
        printNow("There is a door to the west (entryway), a door to the north (bathroom), and a door to the east (bedroom).")
    if room == "bathroom":
        printNow(room.upper())
        printNow("You are in the bathroom.")
        printNow("You are staring at yourself through a water spotted mirror.")
        printNow("There is a medicine cabinet to your left. The sink has been used to wash the blood off something.")
        printNow("The toilet sits to the right of you and there is no toilet paper.")
        printNow("There is only one door to the south (living room).")
    if room == "bedroom":
        printNow(room.upper())
        printNow("You walk into a dark and deserted bedroom.")  
        printNow("To your right there are weird noises coming from behind a closet door.")
        printNow("To your left, underneath the bed, there is some sort of bloody object.")
        printNow("There is only one door to the west (living room), but you can open the closet.")
    if room == "secret room":
        printNow(room.upper())
        printNow("You found a secret room!")
        printNow("You look around and find a single large treasure chest.")
        printNow("Within the chest are several dusty tomes, one of which you take out.")
        printNow("You blow the dust off the book.")
        printNow("The book is titled Programming in Python: A Magical Multimedia Experience.")

#Function used to pick up items through out the game. Items are placed in the players inventory and removed from the available items in the game.
#Arguments are the current room they are in and the item they have requested to pick up.
def takeItem(room, item):
    isItemTaken = false
    global inventory 
    if item in items:
      if items[item] == room:
        inventory = inventory + [item]
        isItemTaken= true 
        del items[item]   
    return isItemTaken

#Function used to read an item in inventory  
def readItem(item): 
    global inventory
    if item in inventory:
      if item == "book":
        printNow("HOW TO SURVIVE A HAUNTED HOUSE")
        printNow("Rule #1 Don\'t enter a haunted house.")
        printNow("Rule #2 Don\'t stop to read anything.")
        printNow("Rule #3 Stay near the entryway.")
        printNow("Rule #4 Find a weapon.")
        printNow("Rule #5 Get out of the haunted house!")
      return true
    return false  

#Function for opening the closet in the bedroom; if you have the knife you survive, otherwise you lose. 
def openCloset():
    global inventory
    if "knife" in inventory: 
        printNow("A monster with a rusty nail bat lunges at you.")
        printNow("You use your knife and defend yourself, defeating the monster.")
        printNow("There appears to be another door in the closet. The monster was guarding something, perhaps.")
        printNow("You can go east (secret room), through the door in the closet.")
        userInput = requestString("Choose a direction")
        userInput = parse(userInput)
        return userInput
    else:
        loseGame()
        return "exit"

def loseGame():
    printNow("A monster with a rusty nail bat lunges at you.")
    printNow("Weaponless, the monster easily bests you. It drags you into the darkness and begins to feast.")

#Called when user enters the secret room.         
def winGame():
    roomDescription("secret room")
    printNow("Congratulations!")
    printNow("You just knew you would find something useful in this house.")
    printNow("The End")
    return "exit"

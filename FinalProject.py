def mainMenu():
    userinput = ""
    while(userinput!= 'exit'):
        printNow("Welcome to the CSIT Guy's Image and Sound Manipulator!")
        printNow("")
        printNow("Please choose what file type you would like to manipulate")
        printNow("Type SOUND to go to our sound manipulator")
        printNow("Type IMAGE to go to our image manipulator")
        printNow("Type EXIT to exit the program")
        printNow("")
        userinput = requestString("Please Enter Your Choice")
        if userinput is None:
          userinput = ""
        userinput = userinput.lower()
        if userinput == 'sound':
            userinput = sound_manipulator()    
        elif userinput == 'image':
            userinput = image_manipulator()       
        elif userinput == 'exit':
            printNow("Thank you for using the CSIT Guy's Manipulator")   
        else:
            printNow("Enter a Correct Choice")
    
            
def image_manipulator():
    userinput = ""
    printNow("\nImage Manipulator")
    printNow("Please start by selecting the picture you would like to manipulate")
    pictureFile = open_picture()
    if pictureFile is None:
        userinput = 'back'
    while (userinput != 'exit' and userinput != 'back'):
        printNow("\nImage Manipulator")
        printNow("Select desired option by entering number")
        printNow("1. Change Picture")
        printNow("2. Cartoonize picture")
        printNow("3. Blend with another picture")
        printNow("4. Checkerboard the Picture")
        printNow("5. Add a border to the Picture")
        printNow("6. Convert image to four colors")
        printNow("7. Save image to a file")
        printNow("Type BACK to the main menu")
        printNow("Type EXIT to exit the program")
        userinput= requestString("Please Enter Your Choice")
        if userinput is None:
          userinput = ""
        userinput = userinput.lower()
        if userinput == '1':
            pictureFile = open_picture()
        elif userinput == '2':
            pictureFile = cartoonize(pictureFile)
        elif userinput == '3':
            printNow("Select picture to blend with")
            pic2 = open_picture()
            if pic2 is not None:
                pictureFile = blend(pictureFile, pic2)
        elif userinput == '4':
            picturefile = coloredCheckerboard(pictureFile)
        elif userinput == '5':
            border = int(input("How big would you like the border to be(1 - 100)?"))
            while (border < 0 or border > 100):
                printNow("You have entered an invalid number!")
                border = int(input("Please enter a border size between 1 and 100"))
            color = 'unknown'
            while (color == 'unknown'):
                printNow("What color would you like the border to be?")
                printNow("Enter 1 for BLACK")
                printNow("Enter 2 for BLUE")
                printNow("Enter 3 for RED")
                printNow("Enter 4 for GREEN")
                printNow("Enter 5 for WHITE")
                choice = requestString("Enter your selection")
                if choice == '1':
                    color = black
                elif choice == '2':
                    color = blue
                elif choice == '3':
                    color = red
                elif choice == '4':
                    color = green
                elif choice == '5':
                    color = white
                else:
                    printNow("Please enter a correct selection")
            pictureFile = add_border(pictureFile, border, color)
        elif userinput == '6':
            pictureFile = four_color(pictureFile)
        elif userinput == '7':
            save_image_file(pictureFile)
        elif userinput == 'exit':
            printNow("Thank you for using the CSIT Guy's Manipulator") 
        elif userinput == 'back':
            userinput = 'back'
        else:    
            printNow("Enter a Correct Choice")
    return userinput
    
    
def sound_manipulator():
    userinput = ""
    printNow("\nSound Manipulator")
    printNow("Please start by selecting the .wav file you would like to manipulate")

    sound_file = open_sound()
    if sound_file is None:
        userinput = 'back'
    while (userinput != 'exit' and userinput != 'back'):
        printNow("\nSound Manipulator")
        printNow("Select desired option by entering number")
        printNow("1. Open a new sound file")
        printNow("2. Change the volume variably")
        printNow("3. Digitze sound")
        printNow("4. Chipmunk sound")
        printNow("5. Slow sound")
        printNow("6. Save Sound to a file")
        printNow("Type BACK to the main menu")
        printNow("Type EXIT to exit the program")
        userinput = requestString("Please Enter Your choice")
        if userinput == '1':
            sound_file = open_sound()
        elif userinput == '2':
            sound_file = changeVolume(sound_file)
        elif userinput == '3':
            sound_file = digitize(sound_file)
        elif userinput == '4':
            sound_file = chipmunk(sound_file)
        elif userinput == '5':
            sound_file = slowspeech(sound_file)
        elif userinput == '6':
            save_sound_file(sound_file)
        elif userinput == 'exit':
            printNow("Thank you for using the CSIT Guy's Manipulator") 
        elif userinput == 'back':
            userinput = 'back'
        else:    
            printNow("Enter a Correct Choice")
    return userinput

def open_picture():
    filename=pickAFile()
    if filename is not None:
      pic=makePicture(filename)
      return pic
    else: 
      return None

def open_sound():
    filename=pickAFile()
    if filename is not None:
      sound=makeSound(filename)
      return sound
    else: 
      return None
 
def save_sound_file(sound):
    folder = pickAFolder()
    userinput= requestString("Enter file name")
    if (folder is not None) and (userinput is not None):
        writeSoundTo(sound, (folder + userinput + ".wav" ))
    else:
        printNow("unable to save file")

def save_image_file(picture):
    folder = pickAFolder()
    userinput= requestString("Enter file name")
    if (folder is not None) and (userinput is not None):
        writePictureTo(picture, (folder + userinput + ".jpg" ))
    else:
        printNow("unable to save file")
    
def blend(pic1, pic2):
    width1, height1 = getWidth(pic1), getHeight(pic1)
    width2, height2 = getWidth(pic2), getHeight(pic2)
    
    
    if width1 > width2:
       width= width2
    else:
       width = width1
    if height1  > height2:
       height = height2 
    else:
       height = height1 
    blendPic = makeEmptyPicture(width, height)
    for y in xrange(height):
        for x in xrange(width):
            targetPx = getPixel(blendPic, x , y )
            px1 = getPixel(pic1, x , y )
            px2 = getPixel(pic2, x , y )
            
            r1 , g1 , b1 =  getRed(px1)  ,  getGreen(px1) ,  getBlue(px1)
            r2 , g2 , b2 = getRed(px2), getGreen(px2), getBlue(px2)
            
            blendColor = makeColor( (r1 + r2)/2, (g1 + g2)/2, (b1 + b2)/2 )
            setColor(targetPx, blendColor)
    show(blendPic)
    return blendPic

#Cartoonize
#Brian
def cartoonize(pic):
    pic = blur(pic, 2, 2)
    pic = colorReducer(pic)
    repaint(pic)
    return pic

#reduces to 256 colors
#Brian
def colorReducer(pic):
  pixels = getPixels(pic)
  for pixel in pixels:
    # 3 bits for red and green 2 for blue
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    nr = int(round(r/(255/7.0))) * (255/7.0)
    ng = int(round(g/(255/7.0))) * (255/7.0)
    nb = int(round(b/(255/3.0))) * (255/3.0)
    if nr>255:
      nr = 255
    if nb>255:
      nb = 255
    color = makeColor(int(nr), int(ng), int(nb))
    
    setColor(pixel,color)
  return pic
  
  
#uses gausian blur
#Brian
def blur(pic, deviation, radius):
    blurredPicture = makeEmptyPicture(getWidth(pic),getHeight(pic))
    #Create empty Table of Weights
    weightTable = [[0 for i in range((2*radius)+1)] for j in range((2*radius)+1)]
    coefficientTable =[[0 for i in range((2*radius)+1)] for j in range((2*radius)+1)]
    #portion of gaussian function that does not change
    constant = 1/(2*math.pi*math.pow(deviation, 2))
    sums = 0
    #indexes in relation to center pixel
    for x in range(-radius, radius+1):
        for y in range(-radius,radius+1):
            #perform gaussian function
            weightTable[x+radius][y+radius] = constant * math.exp(-((math.pow(x,2)+math.pow(y,2))/(2*math.pow(deviation,2))))
            coefficientTable[x+radius][y+radius] = constant * math.exp(-((math.pow(x,2)+math.pow(y,2))/(2*math.pow(deviation,2))))
            sums += weightTable[x+radius][y+radius]  
    inverseSum = 1/sums
    #multiply by the inverse so the sum of all values is 1
    for x in range (0,(2*radius)+1):
        for y in range(0,(2*radius)+1):
            weightTable[x][y] *= inverseSum
    #loops for center pixel x,y
    for x in range(0,getWidth(pic)):
        for y in range(0,getHeight(pic)):
            r = 0
            g = 0
            b = 0
            #check if the center pixel has all neigboring pixels in the radius 
            if(x<radius or y<radius or x>=getWidth(pic)-radius or y>=getHeight(pic)-radius):
       
                xOver = (x+radius) - (getWidth(pic)-1)
                yOver = (y+radius) - (getHeight(pic)-1)
                xUnder = radius-x
                yUnder = radius-y
                if xOver<0:
                    xOver*=0
                if yOver<0:
                    yOver*=0
                if xUnder<0:
                    xUnder*=0
                if yUnder<0:
                    yUnder*=0

                sum2 = 0
                for i in range (-radius+xUnder, radius+1-xOver):
                    for j in range(-radius+yUnder, radius+1-yOver):
                        sum2+=coefficientTable[i+radius][j+radius]
       
                for i in range (-radius+xUnder, radius+1-xOver):
                    for j in range(-radius+yUnder, radius+1-yOver):
                        neighborPixel = getPixel(pic,x+i,y+j)
                        #get color value and multiply by the coresponding weight
                        r += getRed(neighborPixel)*((1/sum2)*coefficientTable[i+radius][j+radius])
                        g += getGreen(neighborPixel)*((1/sum2)*coefficientTable[i+radius][j+radius])
                        b += getBlue(neighborPixel)*((1/sum2)*coefficientTable[i+radius][j+radius])
            #has all pixels within radius     
            else: 
                #loops to get neighboring pixels in radius
                for i in range (-radius, radius+1):
                    for j in range(-radius, radius+1):
                        neighborPixel = getPixel(pic,x+i,y+j)
                        #get color value and multiply by the coresponding weight
                        r += getRed(neighborPixel)*weightTable[i+radius][j+radius]
                        g += getGreen(neighborPixel)*weightTable[i+radius][j+radius]
                        b += getBlue(neighborPixel)*weightTable[i+radius][j+radius]
            pixel = getPixel(blurredPicture, x,y)
            setColor(pixel,makeColor(r,g,b))
    return blurredPicture  
 
  
def four_color(pic):
  valleyGreen = makeColor(34,139,34)
  bayBlue = makeColor(25,25,112) 
  goldenSand = makeColor(189,183,107)
  reddish = makeColor(139,34,34)
  pixels = getPixels(pic)
  for p in pixels: 
    R = getRed(p)
    G = getGreen(p)
    B = getBlue(p)
    luminance = (0.299*R + 0.587*G + 0.114*B) 
    if luminance <64:
      setColor(p, bayBlue)
    elif luminance >=64 and luminance <128:
      setColor(p, goldenSand)
    elif luminance>=128 and luminance <192:
      setColor(p, valleyGreen)
    else:
      setColor(p, reddish)
  repaint(pic)    
  return pic  
    
#Phillip
#Colored Checkerboard
def coloredCheckerboard(pic):
  pixels = getPixels(pic)
  width = getWidth(pic)
  height = getHeight(pic)
  width3=((width/4)+(width/2))
  height3 = ((height/4)+(height/2))
  for x in range(width/4, width/2):
    for y in range(0, height):
      px = getPixel(pic, x, y)
      b = getBlue(px)
      setBlue(px, b * 0)
  for x in range(width/2, width3):
    for y in range(0, height):
      px = getPixel(pic, x, y)
      g = getGreen(px)
      setGreen(px, g * 0)
  for x in range(width3, width):
    for y in range(0, height):
      px = getPixel(pic, x, y)
      r = getRed(px)
      setRed(px, r * 0)
  for x in range(0, width):
    for y in range(0, height/4):
      px = getPixel(pic, x, y)
      r = getRed(px)
      setRed(px, r * 2)
  for x in range(0, width):
    for y in range(height/4, height/2):
      px = getPixel(pic, x, y)
      r = getBlue(px)
      setBlue(px, r * 2)
  for x in range(0, width):
    for y in range(height/2, height3):
      px = getPixel(pic, x, y)
      b = getGreen(px)
      setGreen(px, b * 2)
      r = getRed(px)
      setRed(px, r * 0)
  for x in range(0, width):
    for y in range(height3, height):
      px = getPixel(pic, x, y)
      r = getRed(px)
      setRed(px, r * 2)
      b = getBlue(px)
      setBlue(px, b * 2)
  repaint(pic)
  return pic
  
#Phillip
#Add border of user choice size and color
def add_border(pic, bordersize, color):
  width = getWidth(pic)
  height = getHeight(pic)
  neww = width + bordersize
  newh = height + bordersize
  newpic = makeEmptyPicture(neww, newh)
  pixels = getPixels(newpic)
  for p in pixels:
    setColor(p, color)
  for x in range (0, width):
    for y in range (0, height):
      color=getColor(getPixel(pic, x, y))
      setColor(getPixel(newpic, x + (bordersize/2), y + (bordersize/2)), color)
  repaint(pic)
  return newpic
  
  
#Phillip
#Double, then divide by two sound
def changeVolume(sound):
   for sample in range(0, getLength(sound)/4):
      value = getSampleValueAt(sound, sample)
      setSampleValueAt(sound, sample, value * 2)
   for sample in range(getLength(sound)/4, getLength(sound)/2):
      value = getSampleValueAt(sound, sample)
      setSampleValueAt(sound, sample, value * .5)
   for sample in range(getLength(sound)/2, ((getLength(sound)/2) + (getLength(sound)/4))):
      value = getSampleValueAt(sound, sample)
      setSampleValueAt(sound, sample, value * 2)
   for sample in range(((getLength(sound)/2) + (getLength(sound)/4)), getLength(sound)):
      value = getSampleValueAt(sound, sample)
      setSampleValueAt(sound, sample, value * .5)
   explore(sound)
   return sound
    
#brian
#gives sample a digitized sound by taking the average of samples and assigning it to the four
def digitize(sound):
  sampleRate = int(getSamplingRate(sound))
  newSound = makeEmptySound(getNumSamples(sound),sampleRate)
  for sample in range(0, getLength(sound)-4,4):
      sum = 0
      for i in range(0,4):
        sum += getSampleValueAt(sound, sample+i)
      average= sum/4
      for i in range(0,4):
        setSampleValueAt(newSound, sample+i, average)
  explore(newSound)
  return newSound
  con
def chipmunk(sound):
  samples_count = int(getNumSamples(sound))
  sample_rate = int(getSamplingRate(sound))
  highPitch = makeEmptySound(samples_count, int(sample_rate*1.5))
  index =0
  for sample in range(0,getLength(sound)):
    value = getSampleValueAt(sound, sample)
    setSampleValueAt(highPitch,index,value)
    index+=1
  explore(highPitch)    
  return highPitch
  
def slowspeech(sound):
  samples_count = int(getNumSamples(sound))
  sample_rate = int(getSamplingRate(sound))
  slow_sound = makeEmptySound(samples_count, int(sample_rate*.75))
  index =0
  for sample in range(0,getLength(sound)):
    value = getSampleValueAt(sound, sample)
    setSampleValueAt(slow_sound,index,value)
    index+=1
  explore(slow_sound)    
  return slow_sound  
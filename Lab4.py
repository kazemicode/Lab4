# Sara Kazemi
# Lab 4
# Use the main function (at the end of program)
# to run a test on all defined functions.
# Change output directory to a path that exists
# on your local machine to write files


# Returns the picture given a directory
def getPic():
  return makePicture(pickAFile())

# Writes a picture to a file  
def writePict(pict,name):
  file=getMediaPath(name)
  writePictureTo(pict,file)
  
##################
# Begin Problem 1
##################
# Mirror an image vertically, left to right      
def mirrorVerticalL(picture):
  
  for x in range(0, int(getWidth(picture)/2)):
    for y in range(0 , getHeight(picture)):
      color = getColor(getPixel(picture, x, y))
      setColor(getPixel(picture, getWidth(picture) - x - 1, y), color)
  show(picture)
  return(picture)
  
# Mirror an image vertically, right to left       
def mirrorVerticalR(picture):
  
  for x in range(int(getWidth(picture)/2), getWidth(picture)):
    for y in range(0 , getHeight(picture)):
      color = getColor(getPixel(picture, x, y))
      setColor(getPixel(picture, getWidth(picture) - x - 1, y), color)
  show(picture)
  return(picture)
    

# Mirror an image horizontally, bottom to top        
def mirrorBottomToTop(picture):
  
  for x in range(0, getWidth(picture)):
    for y in range(getHeight(picture)/2 , getHeight(picture)):
      color = getColor(getPixel(picture, x, y))
      setColor(getPixel(picture, x, getHeight(picture) - y - 1), color)
  show(picture)
  return(picture)
  
# Mirror an image horizontally, top to bottom      
def mirrorTopToBottom(picture):
  
  for x in range(0, getWidth(picture)):
    for y in range(0 , getHeight(picture)/2):
      color = getColor(getPixel(picture, x, y))
      setColor(getPixel(picture, x, getHeight(picture) - y - 1), color)
  show(picture)
  return(picture)

# Mirror an image vertically and horizontally 
def QuadMirror(picture):
   ## mirror vertically, right to left
  for x in range(int(getWidth(picture)/2), getWidth(picture)):
    for y in range(0 , getHeight(picture)):
      color = getColor(getPixel(picture, x, y))
      setColor(getPixel(picture, getWidth(picture) - x - 1, y), color)
   ## mirror horizontally, top to bottom
  for x in range(0, getWidth(picture)):
      for y in range(0 , getHeight(picture)/2):
        color = getColor(getPixel(picture, x, y))
        setColor(getPixel(picture, x, getHeight(picture) - y - 1), color)
  
  show(picture)
  return(picture)
##################
# End Problem 1
##################


##################
# Begin Problem 2
##################
# Makes a copy of a given picture
def simpleCopy(inPic):
  mypic = makeEmptyPicture(getWidth(inPic), getHeight(inPic))
  for x in range (0, getWidth(mypic)):
    for y in range (0, getHeight(mypic)):
      setColor(getPixel(mypic, x, y), getColor(getPixel(inPic, x, y)))
  show(mypic)
  return mypic 
##################
# End Problem 2
##################


##################
# Begin Problem 3
##################
# Rotates a picture 90 degrees to the left
def rotatePic(inPic):
  # Swap width and height
  mypic = makeEmptyPicture(getHeight(inPic), getWidth(inPic))
  for y in range (0, getHeight(mypic)):
    for x in range (0, getWidth(mypic)):
      setColor(getPixel(mypic, x, y), getColor(getPixel(inPic, y, x)))
  show(mypic)
  return mypic
##################
# End Problem 3
##################


##################
# Begin Problem 4
##################
# Shrinks a picture by half
def shrink(inPic):
  SHRINK_SIZE = 2 ## shrinking by half
  mypic = makeEmptyPicture(int(getWidth(inPic)/ SHRINK_SIZE), int(getHeight(inPic)/SHRINK_SIZE))
  for x in range (0, getWidth(mypic)):
    for y in range (0, getHeight(mypic)):
      setColor(getPixel(mypic, x, y), getColor(getPixel(inPic, x*SHRINK_SIZE, y*SHRINK_SIZE)))
  show(mypic)
  return mypic
##################
# End Problem 4
##################

################################################################
# The main function performs a test of all functions in Lab 4. 
# Please change dir to your a local path before calling.
################################################################
def main():
  ## Output directory
  dir = "/Documents/CST205/Lab4/output/"
  writePict(mirrorVerticalL(getPic()), dir + "mui_mirror_vertical_LtoR.jpg")
  writePict(mirrorVerticalR(getPic()), dir + "mui_mirror_vertical_RtoL.jpg")
  writePict(mirrorBottomToTop(getPic()), dir + "mui_mirror_horizontol_BtoT.jpg")
  writePict(mirrorTopToBottom(getPic()), dir + "mui_mirror_horizontol_TtoB.jpg")
  writePict(QuadMirror(getPic()), dir + "mui_QuadMirror.jpg")
  writePict(rotatePic(getPic()), dir + "mui_rotated_90.jpg")
  writePict(shrink(getPic()), dir + "mui_shrink.jpg")
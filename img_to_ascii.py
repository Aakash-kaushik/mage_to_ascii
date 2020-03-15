from PIL import Image
import cv2, os, time
import numpy as np
import sys


char_set=["B","S","#","&","@","$","%","*","!",":","."]

#need to adjust the scale accrodingly to your webcam or image in all functions 

def photo_from_path(path):
  img=cv2.imread(path)
  img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  height,width=img.shape
  scale_percent=50
  new_width=int(img.shape[1]*scale_percent/100)
  new_height=int(img.shape[0]*scale_percent/100)
  img=cv2.resize(img,(new_height,new_width))
  img=np.uint8(img/23)

  for c in range(new_width):
    for h in range(new_height):
      print(char_set[img[c,h]],end="")
    print("\n")
  

def photo(arg):
  cap=cv2.VideoCapture(0)
  retval,img=cap.read()
  cap.release()
  #img=cv2.imread("/home/aakash/Pictures/aakash.jpeg")
  img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  height,width=img.shape
  scale=height/float(width)
  new_width=100
  new_height=800
  img=cv2.resize(img,(new_height,new_width))
  img=np.uint8(img/23)

  for c in range(new_width):
    for h in range(new_height):
      print(char_set[img[c,h]],end="")
    print("\n")
    
    
def video():
  cap=cv2.VideoCapture(0)
  while True:
    retval,img=cap.read()
    #cap.release()
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    height,width=img.shape
    scale=height/float(width)
    new_width=100
    #new_height=int(scale*new_width)
    new_height=800
    img=cv2.resize(img,(new_height,new_width))
    img=np.uint8(img/23)

    for c in range(new_width):
      for h in range(new_height):
        print(char_set[img[c,h]],end="")
      print("\n")
    time.sleep(0.08)
    os.system("clear")
    
if __name__=="__main__":
  if len(sys.argv)==2:
    if sys.argv[1]=="webcam_image":
      photo(sys.argv[1])
    if sys.argv[1]=="webcam_video":
      video()
    else:
      photo_from_path(sys.argv[1])
  else:
    print("You specified more than one parameter or didn't specify any")
    


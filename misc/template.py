import math
import sys
import time


#user_thresh = int(sys.argv[3])
if(len(sys.argv) <= 2):
   print("User Error")
   print("     You typed the wrong thing in please check your input")
if(len(sys.argv) == 3):
   user_thresh = 5
if(len(sys.argv) == 4):
   user_thresh = int(sys.argv[3])

#define the files
file_1 = sys.argv[1]
file_2 = sys.argv[2]

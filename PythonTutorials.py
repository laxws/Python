'''name = "Nabil Hakimi"

print (name) # Prints complete string
print (name[0]) # Prints first character of the string
print (name[2:5]) # Prints characters starting from 3rd to 5th
print (name[2:]) # Prints string starting from 3rd character
print (name * 2) # Prints string two times
print (name + "Yusri") # Prints concatenated string

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list) # Prints complete list
print (list[0]) # Prints first element of the list
print (list[1:3]) # Prints elements starting from 2nd till 3rd
print (list[2:]) # Prints elements starting from 3rd element
print (tinylist * 2) # Prints list two times
print (list + tinylist) # Prints concatenated lists

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'jimmy')
print (tuple) # Prints complete tuple
print (tuple[0]) # Prints first element of the tuple
print (tuple[1:3]) # Prints elements starting from 2nd till 3rd
print (tuple[2:]) # Prints elements starting from 3rd element
print (tinytuple * 2) # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (dict['one']) # Prints value for 'one' key
print (dict[2]) # Prints value for 2 key
print (tinydict) # Prints complete dictionary
print (tinydict.keys()) # Prints all the keys
print (tinydict.values()) # Prints all the values'''


import numpy as np
import cv2
from matplotlib import pyplot as plt

imageA = cv2.imread('pcb2.jpg', cv2.IMREAD_COLOR)
imageB = cv2.imread('pcb2_pinhole.jpg', cv2.IMREAD_COLOR)

grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
plt.imshow(imageA, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.imshow(imageB, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
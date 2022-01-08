import time

true = ["T", "t", "True"]
false = ["F", "f", "False"]
correct = 0 #Storing the correct answers

name = input ("What's your name?") #Storing the user's name

print ("\n OK,  +  name + ", let's get started. Remember, the following answers are only True or False.")
time.sleep(2)

print ("\n Paris is the captial of France.")
choice = input(">>> ")
if choice in true:
  correct += 1 #If correct, the user gets one point
else:
  correct += 0
  
print ("\n England is an island.")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0  

print ("\n Northern Ireland isn't part of Great Britian.")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0 
  
print ("\n Andorra is between France and Spain.")
choice = input(">>> ")
if choice in true:
  correct += 1
else:
  correct += 0  
  
print ("\n Iran use to be part of the Perisan Empire.")
choice = input(">>> ")
if choice in true:
  correct += 1
else:
  correct += 0
  
print ("\n Turkmenistan isn't a real country.")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0
    
print ("\n You're finished, " + name +". You got", correct, "out of 6 correct.")
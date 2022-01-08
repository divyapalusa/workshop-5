import random
def guess_random_number(tries,start,stop):
     

    x = random.randint(start, stop)
    print("Please enter only positive integers with in the given range only.Don't enter strs/special symbols/alpha numerics.")

    tries = 5
    print("You have only" ,tries ,"chances ")
    while tries != 0:
        print("Number tries left :", tries)
        tries -= 1
        guess = int(input("Guess a number between 0 and 10: "))
        if x == guess:
            print("You guessed the correct number!")
            break
        elif x > guess:
            print("Guess lower!")
        elif x < guess:
            print("Guess higher!")
        else:
            print("You have failed to guess the number! ")
guess_random_number(5,0,10)

# def guess_random_num_linear(tries,start,stop):


#     x= random.randint(start,stop)
#     print("The number for the program to guess is : ",x)
#     print("The number of tries left : " ,tries )
    
       
#     for i in range(start,stop+1):
#         if i == x:

#             print("The program has guessed the correct number...")
#             return i
    
#         if tries == 0:
#             print("The program has failed to guess the correct number...")

#             return 
        
#         tries -= 1
#         print("The number of tries left : " ,tries )
#         print("The program is guessing...")
            
# guess_random_num_linear(5,0,10)

# def guess_random_num_binary(tries,start,stop):
#     x= random.randint(start,stop)
#     lower_bound = start
#     upper_bound = stop - 1

#     while tries != 0:
#         print("Number of tries left :", tries)
#         tries -= 1

#         mid = (lower_bound + upper_bound) // 2 
#         print("Random number to find is : ",mid)
#         if mid == x:
#             print("Found it! ",x)
#             return mid
#         elif mid < x:
#             lower_bound = mid + 1
#             print("Guess lower!")
#         elif mid > x:
#             upper_bound = mid - 1
#             print("Guess higher")
#         else:
#             print("Your program failed to find the number.")
    
# guess_random_num_binary(5,0,100)
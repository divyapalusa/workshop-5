# declare an unsorted list
unsorted_list = [101, 49, 3, 12, 56]
# define a function named bubblesort with a single parameter of the_list.In it, set up a variable named high_idx that holds the highest index of the passed-in list, which you can derive from subtracting one from its length:
def bubblesort(the_list):
    high_idx = len(the_list) - 1
#   Inside this function, create two loops as follows using nesting and the iteration variables i and j:
    for i in range(high_idx):
        list_changed = False
        for j in range(high_idx):
            item = the_list[j] # Inside the inner loop body, add the following code to retrieve the values for an adjacent pair:
            next = the_list[j+1]
        # Then, check if the value in item is bigger than the value in next. If so, then they are out of order, so their values must be switched so that the higher index has the higher value:
            if item > next:
                the_list[j] = next
                the_list[j+1] = item
                list_changed = True
        # Finally, print the value of the_list, i, and j at the end of each inner loop iteration:
            print(the_list, i, j)
        print(list_changed)
        if list_changed == False:
            break
# call the bubblesort function with the unsorted_list as its argument:
bubblesort(unsorted_list)

 
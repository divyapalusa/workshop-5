def linear_search_dictionary(dictionary,target_value):
    for key in dictionary:
        if dictionary[key] == target_value:
            print(f"Found at key {key}.")
            break
    else:
        print("Target is not in the dictionary.")

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
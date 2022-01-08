def menu(list, question):
    	for item in list:
		print(list.index(item), item)

	while True:
		result = input(question)
		try:
			result = int(result)
			break
		except: 
			print("Selection must be whole number between 0-9:")

	return result

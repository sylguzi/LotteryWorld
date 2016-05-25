from random import randint

def pick_a_number():
	"""Has the user choose a number for their lottery ticket.
	
	Args: (no args)
	
	Returns: Checks if user input is within range and not a letter
	"""
	number = -1;
	while (number < 0 or number > 100):
		try:
			userInput = input("Choose a number from 1-100: ")
			number = int(userInput)
			if (number < 0 or number > 100):
				print("Between 1-100, please. Try again.")
				number = -1
		except ValueError:
			# not a number
			print("Is that really a number? Enter a number please.")
			number = -1
	return number

def compareNumbers(inputNumbers, rng_number):
	"""Compares numbers to each other. 
	
	Args:
		inputNumbers (list): a list of intergers
		rng_number (list): a list of randomly generated intergers
		
	Returns:
		int: how many numbers the user has that matches the rng lotto ticket
	
	Examples:
		>>>compareNumbers([1,2,3,4,5,6,7,8,9,10],[1,2,13,14,15,16,17,18,19,20])
		2 #2 numbers are matching (1 & 2)
		
	"""

	iterate = 0
	matchingNumbers = 0
	winnings = 0
	while iterate < len(inputNumbers):
		if inputNumbers[iterate] in rng_number:
			matchingNumbers += 1
		iterate += 1
	return matchingNumbers
	
def calculateEarnings(MatchingAmount):
	"""Compures how much the user wins per one trial.
	
	Args:
		MatchingAmount (int): how many times user input/generated numbers
		match the rng lottery ticket
	
	Returns:
		int: amount of money the user wins
	
	Examples:
		>>>calculateEarnings(5)
		2500
	"""
	winnings = 0
	if MatchingAmount == 3:
		winnings += 550
	if MatchingAmount == 4:
		winnings += 1500	
	if MatchingAmount == 5:
		winnings += 2500
	if MatchingAmount == 6:
		winnings += 3500		
	if MatchingAmount == 7:
		winnings += 4500
	if MatchingAmount == 8:
		winnings += 5500
	if MatchingAmount == 9:
		winnings += 15000
	if MatchingAmount == 10:
		winnings += 155000
	return winnings
	
def lottery(choice):
	"""The actual lottery game part.
	
	Args:
		choice (int): user choosing what option they want in order to 
		start the program off
	
	Returns:
		list: a list of numbers that the user generates (auto or manual)
	
	Examples:
		>>>lottery(2)
		Please choose either 1 or 2 or 3; other options (like letters) are not valid
		Autogenerate lotto = 1 | Manual lotto = 2 | Simulation lotto = 3:  2
		Choose a number from 1-100:
	
	"""
	user_numbers = []
	rng_number = []
  
	while len(rng_number) < 10:
		number = int(randint(1, 100))
		if number not in rng_number:
			rng_number.append(number)

	if choice == "1":
		tickets = int(input("How many tickets do you want?: "))
		trial = 0
		winnings = 0
		while trial < tickets:
			matchingNumbers = 0
			user_numbers = []
			while len(user_numbers) < 10:
				number = int(randint(1, 100))
				if number not in user_numbers:
					user_numbers.append(number)
			matchingNumbers += compareNumbers(user_numbers, rng_number)
			winnings += calculateEarnings(matchingNumbers)
			trial += 1
		print ("Total winnings: $" + str(winnings))
		return

	elif choice == "2":
		winnings = 0
		matchingNumbers = 0
		while len(user_numbers) < 10:
			number = pick_a_number()
			if number not in user_numbers:
				user_numbers.append(number)
		matchingNumbers += compareNumbers(user_numbers, rng_number)
		winnings += calculateEarnings(matchingNumbers)
		print ("Total winnings: $" + str(winnings))
		return
		
	elif choice == "3":
		totalTrial = int(input("How many trials do you want to run?: "))
		tickets = int(input("How many tickets do you want per trial?: "))
		totalTrialIterator = 0
		netEarnings = 0
		while totalTrialIterator < totalTrial:
			totalTrialIterator+=1
			trial = 0
			winnings = 0
			while trial < tickets:
				matchingNumbers = 0
				user_numbers = []
				while len(user_numbers) < 10:
					number = int(randint(1, 100))
					if number not in user_numbers:
						user_numbers.append(number)
				matchingNumbers += compareNumbers(user_numbers, rng_number)
				winnings += calculateEarnings(matchingNumbers)
				trial += 1
			netEarnings += winnings

		print ("The average amount won per trial was: $" + str(netEarnings / totalTrial))
		return

	print ("Please choose either 1 or 2 or 3; other options (like letters) are not valid")
	choice = input("Autogenerate lotto = 1 | Manual lotto = 2 | Simulation lotto = 3: ")
	lottery(choice)
	
	return (user_numbers)

print ("Welcome to lotto world! See if you can match any numbers together~")
print ("You need to match 3-10 numbers with the randomly-generated lottery ticket in order to win.")
print ("")
print ("-----------------------------------------")
print ("|3 matches = $550      4 matches = $1500|")
print ("|5 matches = $2500     6 matches = $3500|")
print ("|7 matches = $4500     8 matches = $5500|")
print ("|9 matches = $15000 10 matches = $155000|")
print ("-----------------------------------------")
print ("")
print ("Best of luck, and may the odds be ever in your favor :)")
print ("")

choice = input("Autogenerate lotto = 1 | Manual lotto = 2 | Simulation lotto = 3: ")
lottery(choice)
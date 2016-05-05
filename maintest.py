from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#INSTALL THESE -->

#sudo pip install fuzzywuzzy
#sudo pip install python-Levenshtein

def input():
	command = raw_input("What's your command? ")
	return command

def main():
	switch = 1

	while(switch == 1):
		usercommand = input()
		choices = ["wash dishes", "making bed", "taking out trash", "vacuuming", "cooking food", "doing laundry", "dusting", "lawn mowing"]
		print(process.extract(usercommand, choices, limit=8))
		results = process.extract(usercommand, choices, limit=8)
		match = results[0]
		print("\n")
		print("Your input matches this command:")
		print(match[0])
		print("\n" + "Exit program? (y / n)")
		userexit = raw_input()	
		if userexit == "y":
			switch = 0

	return 
    
if __name__ == '__main__':
    main()
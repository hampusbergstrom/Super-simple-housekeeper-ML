from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#INSTALL THESE -->

#sudo pip install fuzzywuzzy
#sudo pip install python-Levenshtein

def input():
	command = raw_input("What's your command? ")
	return command

def main():
	usercommand = input()
	choices = ["dishwashing", "making bed", "taking out trash", "vacuuming", "cooking food", "doing laundry"]
	print(process.extract(usercommand, choices, limit=8))
	
	#print(fuzz.ratio("damsuga", "dammsuga"))
	#choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
	#print(process.extract("new york jets", choices, limit=8))
    #print(process.extractOne("cowboys", choices))
	return 
    
if __name__ == '__main__':
    main()
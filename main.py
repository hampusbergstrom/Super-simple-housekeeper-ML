from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import json
from handleInputFromUser import *
from databaseFunctions import inputToDatabaseHandler


#load the Jsonfile and try it against the input string
def getKeyAndValueFromJson(input_string):

    with open('commands.json', 'r') as json_file:
        data = json.load(json_file)
        json_file.close()

    for key in data.items():
        current_key = key[0]
        for value in key[1]:
            if (value == input_string):
                print "\n" + value + " " + "will be done Sir!"
                return True

    return False

#Check if this is what the user intended with the command
def correctChore(input_result):

    for i in range(0, len(input_result[0])):
        match_result = input_result[0][i]

        print("\n Your input matches this result: " + match_result[0] + "\n")
        print("Is this what you intended? \n")

        if (correctHelperForAnswer() == "correctCommand"):

            inputToDatabaseHandler(match_result, input_result)

            return True

        print "Trying next chore...\n"

    print "Please try another type or chore....\n"

#Check the type of household chore
def whatTypeOfChore():

    #TODO:input algorithm to filter the sentence from unneccessary words.

    input_string = getInputAndCheckIntention()

    if (input_string == "resetdb"):
        return True
    else:
        if (getKeyAndValueFromJson(input_string) == False):
            result = (process.extract(input_string, commands, limit=8))
            return (result, input_string)
        else:
            return True

#Make logic run
def startHouseholdRobot():

    input_result = whatTypeOfChore()

    if (input_result == True):
        return True
    else:
        correctChore(input_result)

def main():

    while True:
        startHouseholdRobot()

if __name__=='__main__':
    main()

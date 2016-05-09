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
def correctChore():

    input_result = checkChore()
    for i in range(0, len(input_result[0])):
        match_result = input_result[0][i]
        print("\n Your input matches this result: " + match_result[0] + "\n")
        print("Is this what you intended? \n")
        if (correctHelperForAnswer() == "correctCommand"):

            inputToDatabaseHandler(match_result, input_result)

            print input_result

            checkChore()

        print("Trying next chore..")

#Check the type of household chore
def checkChore():

    input_string = getInputAndCheckIntention()

    #TODO:input algorithm to filter the sentence from unneccessary words.

    if (getKeyAndValueFromJson(input_string) == False):
        result = (process.extract(input_string, commands, limit=8))
        return (result, input_string)

    return correctChore()

def startRobot():
    correctChore()

def main():

    startRobot()

if __name__=='__main__':
    main()

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import sys
import json
from pprint import pprint

#Handling the exit of the program when it should be exited
def handleExit():
    sys.exit()

#Saving input if it is a string
def inputCommand():

    command = raw_input("Enter command, exit to close: ")

    if (command == "exit"):
        handleExit()
    elif (isinstance(command, basestring)):
        return command.lower()
    else:
        print "Enter a string: "

#Subfunction checking what user actually intended with the command
def correctHelperForAnswer():

        answer = raw_input("Input: y/n \n")

        if (answer == "y"):
            return "correctCommand"
        elif (answer == "n"):
            return
        else:
            print "Please type y or n"

#load the Jsonfile and try it against the input string
def getKeyAndValueFromJson(input_string):

    with open('commands.json') as json_file:
        data = json.load(json_file)

        for key in data.items():
            current_key = key[0]

            for value in key[1]:
                if (value == input_string):
                    print "\n" + value + " " + "will be done Sir!"
                    return True

        return False

#Check if this is what the user wanted with the command
def correctChore():

    input_result = checkChore()

    for i in range(0, len(input_result)):
        match_result = input_result[i]

        print("\n Your input matches this result: " + match_result[0] + "\n")
        print("Is this what you intended? \n")
        if (correctHelperForAnswer() == "correctCommand"):
            #TODO:Save starting input from user to the loadfile
            break
        print("Trying next chore..")

#Check the type of household chore
def checkChore():
    #TODO:input algorithm to filter the sentence from unneccessary words.
    #TODO: check wheter the command exists in jsonfile, and then run it
    #else run the algorithm
    commands = ["washing the dishes", "making bed", "taking out trash", "vacuuming",
                "cooking food", "doing laundry", "dusting", "lawn mowing"]

    input_string = inputCommand()

    if (getKeyAndValueFromJson(input_string) == False):
        result = (process.extract(input_string, commands, limit=8))
        return result
    else:
       correctChore()

def main():

    while True:
        correctChore()

if __name__=='__main__':
    main()

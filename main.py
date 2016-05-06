from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import sys
import commandClasses

#Handling the exit of the program when it should be exited
def handleExit():
    sys.exit()

#Saving input if it is a string
def inputCommand():

    command = raw_input("Enter command, exit to close: ")

    if (command == "exit"):
        handleExit()
    elif (isinstance(command, basestring)):
        return command
    else:
        print "Enter a string: "

#Subfunction checking what user actually intended with the command
def correctHelperForAnswer():

        answer = raw_input("Input: Y/N \n")

        if (answer == "Y"):
            return "correctCommand"
        elif (answer == "N"):
            return
        else:
            print "Please type Y or N"

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
    commands = ["washing the dishes", "making bed", "taking out trash", "vacuuming",
                "cooking food", "doing laundry", "dusting", "lawn mowing"]

    input_string = inputCommand()

    result = (process.extract(input_string, commands, limit=8))

    return result

def main():

    while True:
        correctChore()

if __name__=='__main__':
    main()

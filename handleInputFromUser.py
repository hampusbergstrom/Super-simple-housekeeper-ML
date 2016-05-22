import sys
import json
from pprint import pprint
from databaseFunctions import *

#Subfunction checking what user actually intended with the command
def correctHelperForAnswer():

        answer = raw_input("Input: y/n \n")

        if (answer == "y"):
            return "correctCommand"
        elif (answer == "n"):
            return
        else:
            print "Please type y or n"

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

#Check whether exact input already exists in the json database
def checkUserInputToJson(input_string):
    #Loading database
    data = openDatabaseFileCLF('X_train.json')

    #Initiate training set
    dbcommands = []

    #Building training_set and y_train
    for x in range(0, 8):
        classnumber = str(x)
        for y in range(0, len(data[classnumber])):
            dbcommands.append(data[classnumber][y])

    for command in dbcommands:
        if input_string == command:
            print "\n" + input_string + " " + "will be done Sir!"
            return True

#Wrapping all of the input type functions to one single function
#Put all functions belonging to Input in this one
def getInputAndCheckIntention():

    input_string = inputCommand()

    if (input_string == "resetdb"):
        resetDB()
        return "resetdb"
    else:
        input_result = checkUserInputToJson(input_string)
        return input_string, input_result



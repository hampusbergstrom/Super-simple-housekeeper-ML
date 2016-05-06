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

#Check if this is what the user wanted with the command
def correctChore():

    input_result = checkChore()
    for i in range(0, len(input_result[0])):
        match_result = input_result[0][i]

        print("\n Your input matches this result: " + match_result[0] + "\n")
        print("Is this what you intended? \n")
        if (correctHelperForAnswer() == "correctCommand"):
            #TODO:Save starting input from user to the loadfile
            
            #Reads database file
            with open('commands.json', 'r') as json_file:
                data = json.load(json_file)
                json_file.close()

            #Appends new user_command to json data
            data[match_result[0]].append(input_result[1])

            #prints data of selected command class
            print data[match_result[0]]

            #Writes new data to database file
            with open('commands.json', 'w') as json_file:
                json_file.write(json.dumps(data))
                json_file.close()

            #Reads database file to check if the new command was written to file
            with open('commands.json', 'r') as json_file:
                data2 = json.load(json_file)
                print "\n", data2[match_result[0]][len(data2[match_result[0]]) - 1]
                json_file.close()        
            
            break
        print("Trying next chore..")

#Check the type of household chore
def checkChore():
    #TODO:input algorithm to filter the sentence from unneccessary words.
    #TODO: check wether the command exists in jsonfile, and then run it
    #else run the algorithm
    commands = ["wash the dishes", "make the bed", "take out the trash", "vacuum the floor",
                "cook food", "do laundry", "do some dusting ", "mow the lawn"]

    input_string = inputCommand()
    resetinput = input_string
    if(resetinput == "resetdb"):    
        resetDB()
        return
    #Checks directly if command matches the default commands
    for command in commands:
        if input_string == command:
            print "\n" + input_string + " " + "will be done Sir!"
            return correctChore()

    if (getKeyAndValueFromJson(input_string) == False):
        result = (process.extract(input_string, commands, limit=8))
        return (result, input_string)
    else:
       correctChore()

def resetDB():
            #Reads database file
            with open('commandsbackupreplacement.json', 'r') as json_file:
                resetdata = json.load(json_file)
                json_file.close()

            #Writes default data to database
            with open('commands.json', 'w') as json_file:
                json_file.write(json.dumps(resetdata))
                json_file.close()

            print "Database has been reset!"
            return correctChore()  

def main():

    while True:
        correctChore()

if __name__=='__main__':
    main()

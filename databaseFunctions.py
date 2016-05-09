import json

#Reset the database input values saved from users over time
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

#Reads database file
def openDatabaseFile():

    with open('commands.json', 'r') as json_file:
        data = json.load(json_file)
        return data
        json_file.close()

#Append and write input from user to database
def writeCorrectInputToDatabase(match_result, input_result):

    data = openDatabaseFile()

    data[match_result[0]].append(input_result[1])

    with open('commands.json', 'w') as json_file:
        json_file.write(json.dumps(data))
        json_file.close()

#Reads database file to check if the new command was written to file
def confirmationOfDatabaseInput(match_result):

    with open('commands.json', 'r') as json_file:
        data2 = json.load(json_file)
#        print "\n", data2[match_result[0]][len(data2[match_result[0]]) - 1]
        json_file.close()

#Wrapping the write to database functions
def inputToDatabaseHandler(match_result, input_result):

    writeCorrectInputToDatabase(match_result, input_result)
    confirmationOfDatabaseInput(match_result)


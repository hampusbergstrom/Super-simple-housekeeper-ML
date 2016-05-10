import json
import re
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

    if match_result[0] == "do some dusting ":
        newarray = ""
        for i in range(0, len(match_result[0])-1):
            newarray += match_result[0][i]
        data[newarray].append(input_result[1])

    else:
        data[match_result[0]].append(input_result[1])

    with open('commands.json', 'w') as json_file:
        json_file.write(json.dumps(data))
        json_file.close()

#Reads database file to check if the new command was written to file
def confirmationOfDatabaseInput(match_result):
    
    if match_result[0] == "do some dusting ":
        newarray = ""
        for i in range(0, len(match_result[0])-1):
            newarray += match_result[0][i]

        with open('commands.json', 'r') as json_file:
            data2 = json.load(json_file)
            print "\n", data2[newarray][len(data2[newarray]) - 1]
            json_file.close()
        return
    else:
        with open('commands.json', 'r') as json_file:
            data2 = json.load(json_file)
            print "\n", data2[match_result[0]][len(data2[match_result[0]]) - 1]
            json_file.close()
        return

#Wrapping the write to database functions
def inputToDatabaseHandler(match_result, input_result):

    writeCorrectInputToDatabase(match_result, input_result)
    confirmationOfDatabaseInput(match_result)

#Populates the initial ignorelist based on database
def initializeIgnoreList():

    #resetDB()
    commands = openDatabaseFile()

    #Loads file
    with open ('ignorelist.json', 'r') as json_file:
        ignoredata = json.load(json_file)
        json_file.close()

    wordSet = set()

    #Filters words
    for i in commands:
        currentSet = set()

        for j in commands[i]:
            wordList = re.sub("[^\w]", " ",  j).split()

            for word in wordList:
                if (word not in ignoredata["list"]):
                    currentSet.add(word)

        for word in currentSet:
            if (word in wordSet):
                ignoredata["list"].append(word)
            else:
                wordSet.add(word)

    #Saves file
    with open('ignoreList.json', 'w') as json_file:
        json_file.write(json.dumps(ignoredata))
        json_file.close()

#Fetches the list of ignored words
def getIgnoreList():

    with open ('ignorelist.json', 'r') as json_file:
        data = json.load(json_file)
        print(data)
        return data
        json_file.close()

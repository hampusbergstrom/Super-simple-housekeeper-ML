from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import json
from handleInputFromUser import *
from databaseFunctions import inputToDatabaseHandler
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer


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

        #instantiate classifier and vectorizer
        clf = MultinomialNB(alpha = 0.01)
        #vectorizer = TfidfVectorizer(min_df = 1, ngram_range = (1, 2))

        vectorizer = CountVectorizer(analyzer = "word",
                                        tokenizer = None,
                                        preprocessor = None,
                                        stop_words = None,
                                        max_features = 1000)

        data = openDatabaseFileCLF('X_train.json')
        
        #Initiate training set
        training_set = []

        #Initiate y_train (Label Ids)
        y_train = []

        #Building training_set and y_train
        for x in range(0, 8):
            classnumber = str(x)
            for y in range(0, len(data[classnumber])):
                y_train.append(x)
                training_set.append(data[classnumber][y])
        print training_set
        print y_train

        '''
        #### OLD TRAINING SET ####
        #Apply vectorizer to training data
        training_set_old = ["wash the dishes", "can you please wash the dishes", "please dish me bro", "can you clean up the dishes?", "can you take care of the dishes?", "do the dishes please",
                    "make the bed", "can you make the bed?", "can you change the sheets?", "please make the bed", "can you please make the bed?",
                    "take out the trash", "can you throw the trash out?", "can you empty the bin?",
                    "vacuum the floor", "can you vacuum the house?", "can you do some vacuuming?", "do you mind bringing out the hoover and doing some cleaning?", "please vacuum the living room",
                    "cook food", "can you make me some food?", "do some cooking please", "can you prepare a meal?", "arrange some cooking por favor",
                    "do laundry", "do the laundry!", "clean my clothes please", "please take care of my laundry",
                    "do some dusting", "can you remove all the dust from the shelves?", "do some dusting", "dust dust dust",
                    "mow the lawn", "cut the grass", "mow the lawn"]
        '''

        #Apply vectorizer to training data
        X_train = vectorizer.fit_transform(training_set)
                

        #Labels
        y_train_labels = [(0, 'wash the dishes'), (1, 'make the bed'), (2, 'take out the trash'), (3, 'vacuum the floor'), (4, 'cook food'), (5, 'do laundry'), (6, 'do some dust'), (7, 'mow the lawn')]

        #Train classifier
        clf.fit(X_train, y_train)

        #Predict string
#        print 'Enter input string: \n'
#        input_string = raw_input()

        #Array result with label ID
        resultLabel = clf.predict(vectorizer.transform([input_string]))

        #Printing result
        print "\n## PREDICTING INPUT STRING WITH NAIVE BAYES ALGORITHM##\n"

        print 'input string: ', input_string + "\n"
        print 'predict label ID: ', resultLabel
        print 'predict label name: ', y_train_labels[resultLabel[0]]
        print 'predict probabilities for Naive Bayes',  clf.predict_proba(vectorizer.transform([input_string]))

        print "\n\n## PREDICTING INPUT STRING WITH KNN ALGORITHM ##\n"

        clf3 = KNeighborsClassifier(n_neighbors = 10)

        clf3.fit(X_train, y_train)

        resultLabel3 = clf3.predict(vectorizer.transform([input_string]))

        print 'predict label: ', resultLabel3
        print 'predict label name: ', y_train_labels[resultLabel3[0]]
        print 'predict probabilities for KNN',  clf3.predict_proba(vectorizer.transform([input_string]))

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

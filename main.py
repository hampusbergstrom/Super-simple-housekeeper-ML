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

#Check the type of household chore
def whatTypeOfChore():

    #TODO:input algorithm to filter the sentence from unneccessary words.
    input_result = getInputAndCheckIntention()

    #If input_string is already in database, return
    if input_result[1]:
        return

    if (input_result[0] == "resetdb"):
        return True
    else:

        initializeIgnoreList()
        #instantiate classifier and vectorizer
        clf = MultinomialNB(alpha = 0.01)
        #vectorizer = TfidfVectorizer(min_df = 1, ngram_range = (1, 2))

        vectorizer = CountVectorizer(analyzer = "word",
                                        tokenizer = None,
                                        preprocessor = None,
                                        stop_words = getIgnoreList(),
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
        
        #Printing not neccesary
        #print training_set
        #print y_train

        #Apply vectorizer to training data
        X_train = vectorizer.fit_transform(training_set)

        #Labels
        y_train_labels = [(0, 'wash the dishes'), (1, 'make the bed'), (2, 'take out the trash'), (3, 'vacuum the floor'), (4, 'cook food'), (5, 'do laundry'), (6, 'do some dust'), (7, 'mow the lawn')]

        #Train classifier
        clf.fit(X_train, y_train)

        #Array result with label ID
        resultLabel = clf.predict(vectorizer.transform([input_result[0]]))

        #Printing result
        print '-----------------------------------------------------------'
        print 'Prediction for the Naive Bayes algorithm and KNN'
        print "\n## PREDICTING INPUT STRING WITH NAIVE BAYES ALGORITHM##\n"

        print 'input string: ', input_result[0] + "\n"
        print 'predict label ID: ', resultLabel
        print 'predict label name: ', y_train_labels[resultLabel[0]]
        print 'predict probabilities for Naive Bayes',  clf.predict_proba(vectorizer.transform([input_result[0]]))

        print "\n\n## PREDICTING INPUT STRING WITH KNN ALGORITHM ##\n"

        clf3 = KNeighborsClassifier(n_neighbors = 10)

        clf3.fit(X_train, y_train)

        resultLabel3 = clf3.predict(vectorizer.transform([input_result[0]]))

        print 'predict label: ', resultLabel3
        print 'predict label name: ', y_train_labels[resultLabel3[0]]
        print 'predict probabilities for KNN',  clf3.predict_proba(vectorizer.transform([input_result[0]]))


        print '----------------------------------------------------------------'
        print 'Your input was predicted to this result: ', y_train_labels[resultLabel3[0]]
        print 'Do you want to save this to the database?'
        print '(Saving to the database means that the exact command written again'
        print 'instant parses to the command done by the household robot)'
        print 'Reseting the database can be done with: "resetdb" command'
        #Writes input_string to correct class in database
        if  (correctHelperForAnswer() == "correctCommand"):
            writeToDatabase(input_result[0], str(resultLabel[0]))
            print "\n" + input_result[0] + " " + "will be done Sir!"
        return True

#Make logic run
def startHouseholdRobot():

    input_result = whatTypeOfChore()

    if (input_result == True):
        return True

def main():

    while True:
        startHouseholdRobot()

if __name__=='__main__':
    main()

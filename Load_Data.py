import csv


currentuser={}

def printUsers(dataDump):
    counter = 0
    for x in dataDump:
        counter += 1
        print(counter, "-", str.title(x["ï»¿Name"]))
    return


def csvOpenAndExtra():
    dataDump = []

    #opens the CSV file as a dictionary
    print("-----------------------------")
    with open('checkIn_csv_testing.csv', mode='r+') as csv_file:
        file = open("checkIn_csv_testing.csv")
        csvreader = csv.DictReader(file)

    #ALL data(dictionaries in a list) from csv dumped into a new list
    for row in csvreader:
        dataDump.append(row)
    print("select a user:")

    #print usernames and nums ( 1- Tom)
    printUsers(dataDump)

    #creating new dictionary for the single user:
    print("'''''''''''''''''''")
    while True:
        try:
            pickuser= int(input("Enter a number to pick a user:"))-1
            for i in dataDump[pickuser]:
                currentuser[i] = dataDump[pickuser][i]
            break
        except:
            print("That an invalid select, Please try again")
            True

    dataDump.clear() #erasing dataDump




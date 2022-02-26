from Load_Data import currentuser
from datetime import datetime
import csv

#Option 3

def Heading_editdata():
    print("\n------------------------")
    print("--Edit Sign In/Out Times--")
    print("------------------------")
    print(str.upper(currentuser['ï»¿Name'])+"'s times:" )
    Menu_editData()

def Menu_editData():
    i = 1
    for x in currentuser:
        # skip info(username, password, name) in dictionary until days
        if x == 'ï»¿Name' or x == 'Username' or x == 'Password':
            continue

        # print DayIN/OUT + time
        print(str(i) + "-", x + ":", currentuser[x])
        i += 1

    message = "Which do you want to change? Enter a number between 1-"+str(i-1)
    selecting_key(input(message))

def selecting_key(n):
    counter=0
    placeholder=""

    for x in currentuser:
        # skip info(username, password, name) in dictionary until days
        if x == 'ï»¿Name' or x == 'Username' or x == 'Password':
            continue

        placeholder = x #placeholder with take the key
        counter+=1

        #stop when counter matches user input
        if counter == int(n):
            break

    print("you selected",placeholder)
    openCSV_MakeDict(placeholder)

def openCSV_MakeDict(placeholder):
    # Open csv/ make dict (csvreader)
    timeInputTest=""
    with open ("checkIn_csv_testing.csv","r+") as csvfile:
        csvreader=csv.DictReader (csvfile)
        #csvfile.close()##############not working

    #search the new dict for username
        for v in csvreader:
            print(v)
            if currentuser['ï»¿Name'] in v['ï»¿Name']:
                timeInputTest=timeValidation()
                print("transfered back",timeInputTest)
                print("testing ",v[placeholder])
                v[placeholder]=timeInputTest
                print("testing after updated ", v[placeholder])

        print("UPDATED!")
        tes(csvreader)

        #return currentuser


def timeValidation():
    while True:
        try:
            timeInputTest = input("enter a new time (hh:mm)")
            date_time_obj = datetime.strptime(timeInputTest, '%H:%M')
            print(date_time_obj)
            return timeInputTest
        except:
            print("Invalid time")

def tes(csvreader):
    print("tes.....................")
    print(csvreader)
    for x in csvreader:  ##########NOT PRINTING
        print(x)  #################

"""
def cameraspeedcheck():
    timeformat = "%H:%M:%S"
    caminput1 = input("At what time did sensor 1 actuate? ")
    try:
        validtime = datetime.datetime.strptime(caminput1, timeformat)
        # Do your logic with validtime, which is a valid format
    except ValueError:
# Do your logic for invalid format (maybe print some message?).

"""
#write dictionary






def edit_selected_day(placeholder):
    print("here"
          "")
    dataDump={}
    print("-----------------------------")
    with open('checkIn_csv_testing.csv', mode='r+') as csv_file:
        file = open("checkIn_csv_testing.csv")
        csvreader = csv.DictReader(file)

    #ALL data(dictionaries in a list) from csv dumped into a new list
    for row in csvreader:
        dataDump.append(row)



    #fieldnames = ['ï»¿Name', 'Username', 'Password', "MonIn", "MonOut", "TueIn", "TueOut", "WedIn", "WedOut", "ThuIn",
              #    "ThuOut", "FriIn", "FriOut"]

    #with open('checkIn_csv_testing.csv', 'w') as csv_file: #,newline=" " removed

    #writer = csv.DictWriter(csv_file, fieldnames=fieldnames)




#https://stackoverflow.com/questions/11033590/change-specific-value-in-csv-file-via-python
  #  print("-----------------------------")
   # with open('checkIn_csv_testing.csv', 'w') as csv_file: #,newline=" " removed
    #

        #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        #file = open("checkIn_csv_testing.csv")
        #csvwriter  = csv.DictWriter(csv_file)
        #csvwriter = csv.DictWriter(csv_file, fieldnames=fieldnames)

       # print(csvwriter)

        #csvwriter.writeheader()
        #csvwriter.writerow({'MonIn': '12:53', 'MonOut': '16:10'})
        #csvwriter.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        #csvwriter.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

####load csv

"""
# Here your csv file
    r = csv.DictWriter(open('checkIn_csv_testing.csv'))
    print(r)
#maybe dictionary is better
    for i in r:
        print(i)
    #if currentuser['ï»¿Name'] in i:
      #  print(currentuser['ï»¿Name'], "is here", i)

       # csvreader = csv.DictWriter()
       """
"""  """
   # with open('checkIn_csv_testing.csv', mode='w') as csv_file:
      #  file = open("checkIn_csv_testing.csv")

#tryin to use pickuser but might be better to use a in list
    #find person by searching

    # day selected


#def editSignInSignOut():
 #   print("------------------------")
  #  input("Press 'Enter' to return to the menu screen")



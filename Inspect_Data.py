from datetime import datetime
from Load_Data import currentuser

#Option 2- check the sign in/out times
def Heading_checkTimes():
    print("\n--------------------------------")
    print("-------Check In/Out Times-------")
    print("--------------------------------")
    print("LOGGED IN AS:", str.upper(currentuser['ï»¿Name']))
    print("\n")
    checkSignInSignOut()

def checkSignInSignOut():
    i = 0
    totalTime=[]
    InOutSumList = []

    for x in currentuser:
        #skip info(username, password, name) in dictionary until days
        if x == 'ï»¿Name' or x == 'Username' or x == 'Password':
            continue

        #print DayIN/OUT + time
        print(x + ":  ", currentuser[x])
        i +=1

        #create a list of
        InOutSumList.append(currentuser[x])

        starttime = datetime.strptime(currentuser[x], "%H:%M")

        if i == 2:
            n=datetime.strptime(InOutSumList[1], "%H:%M")- datetime.strptime(InOutSumList[0], "%H:%M")
            totalTime.append(n)
            print("Total :  ",str(n)[:-3],"hr/min")
            InOutSumList.clear()
            print("\n")
            i=0

    totalTimePerWeek(totalTime)

def totalTimePerWeek(totalTime):
    mins= sum([d.seconds for d in totalTime]) /60 % 60.0
    hrs= sum([d.seconds for d in totalTime]) / 60.0 //60.0
    print("--------------------------------")
    print("--------------------------------")
    print("Total time per week:")
    print("hrs:",hrs)
    print("mins:", mins)
    print("--------------------------------")
    print("--------------------------------")
    input("Press 'Enter' to return to the menu screen")
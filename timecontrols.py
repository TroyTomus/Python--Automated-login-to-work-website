import random

refreshRate= 45 #refresh every the while Loop every ... seconds

timeNow = time.ctime()
timeDay = timeNow [0:3]
timeMonth = timeNow [4:7]
timeHrMin = timeNow [11:16]
timeYear = timeNow [20:24]

secs12hrs= 60*60*12
FMT = "%H:%M"

def timeLoopChecker(day):
    print("_____timeLoopChecker()_____")
    print("Today is",day+".\nIt's a work day. Now checking the time...")
    print("---------------------------")
    while True:
        timeNow = time.ctime()
        delay = random.randint(20, 120)
        print("Today's sign in time:",signInTimes[day])
        if timeNow [11:16] == signInTimes[day]:
            print("Delayed for:",delay)
            time.sleep(delay)
            print("The time is: ",timeNow)
            print("PARTY TIME!")
            break
        else:
            print("It's not time yet. It's only:", timeNow [11:16])
        print("Refresh in:", refreshRate,"seconds\n")
        time.sleep(refreshRate)

def dayLoopChecker():
    print("_____dayLoopChecker()_____")
    print("Checking the day...")
    try:
        if timeDay == "Sun" or timeDay == "Sat":
            print("It's the weekend. The program will check again in 12hrs")
            time.sleep(secs12hrs)
        elif timeDay == "Mon":
            timeLoopChecker("Mon")
        elif timeDay == "Tue":
            timeLoopChecker("Tue")
        elif timeDay == "Wed":
            timeLoopChecker("Wed")
        elif timeDay == "Thu":
            timeLoopChecker("Thu")
        elif timeDay == "Fri":
            timeLoopChecker("Fri")
        else:
            raise KeyError ("we have an error in the 'dayChecker()', if")
        print("dayChecker function:", day)
    except:
        print("we have an error!")


#WIP##############################################
def refreshRateCalculator(startTime,currenttime):
    startTime="16:05"
    currenttime="16:00"
    TimeRemainingMin=(int(startTime[:2])*60)-(60*int(currenttime[:2]))+(int(startTime[4:]))-(int(currenttime[4:]))
    if TimeRemainingMin <0: #add 24hrs in secs
        TimeRemainingMin += 1440
        print("Mins until start:", TimeRemainingMin)
        print("Secs until start:", TimeRemainingMin * 60)
        return TimeRemainingMin
    elif TimeRemainingMin >= 0:
        print("Mins until start:", TimeRemainingMin)
        TimeRemainingMin = TimeRemainingMin*60
        print("Secs until start:", TimeRemainingMin)
        return TimeRemainingMin
#refreshRateCalculator(1,2)

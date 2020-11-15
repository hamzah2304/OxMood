import json
import re
import datetime

file = open("Oxlove3New.txt", "r")
contents = file.read()
contents = contents.split("\n")
newRecords = []
newFile = open("Oxlove3Reformatted.txt", "w")
for thing in contents:
    record = json.loads(thing)
    currentDate = datetime.date.today()
    date = record[2]
    regex1 = "[1-9] h"
    checker1 = re.compile(regex1)
    regex2 = "[1-9] d"
    checker2 = re.compile(regex2)
    regex3 = "[1-9][1-9] [A-Z][a-z]* at [1-9][1-9]:[1-9][1-9]"
    checker3 = re.compile(regex3)
    if checker1.match(date):
        date = currentDate.strftime("%Y/%m/%d")
    elif checker2.match(date):
        currentDate -= datetime.timedelta(int(date[0]))
        date = currentDate.strftime("%Y/%m/%d")
    else:
        splitDate = date.split()
        if splitDate[1] == "January":
            date = f"2020/01/{splitDate[0]}"
        elif splitDate[1] == "February":
            date = f"2020/02/{splitDate[0]}"
        elif splitDate[1] == "March":
            date = f"2020/03/{splitDate[0]}"
        elif splitDate[1] == "April":
            date = f"2020/04/{splitDate[0]}"
        elif splitDate[1] == "May":
            date = f"2020/05/{splitDate[0]}"
        elif splitDate[1] == "June":
            date = f"2020/06/{splitDate[0]}"
        elif splitDate[1] == "July":
            date = f"2020/07/{splitDate[0]}"
        elif splitDate[1] == "August":
            date = f"2020/08/{splitDate[0]}"
        elif splitDate[1] == "September":
            date = f"2020/09/{splitDate[0]}"
        elif splitDate[1] == "October":
            date = f"2020/10/{splitDate[0]}"
        elif splitDate[1] == "November":
            date = f"2020/11/{splitDate[0]}"
        else:
            date = f"2020/12/{splitDate[0]}"
    record[2] = date

    newFile.write(json.dumps(record) + "\n")
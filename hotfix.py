import json
file = open("Oxlove3.txt", "r")
contents = file.read()
contents = contents.split("\n")
newRecords = []
newFile = open("Oxlove3New.txt", "w")
for thing in contents:
    print(thing)
    record = json.loads(thing)
    newRecord = (
        record["Initials"],
        record["College"],
        record["DateOfPost"],
        record["Hashtag"],
        record["Content"],
        record["NameOfPage"]
    )
    newFile.write(json.dumps(newRecord) + "\n")



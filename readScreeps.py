import screepsapi
import json

def writeGraphite(prefix, value):
    print(prefix + ": " + str(value))

def outputDict(prefix, data):
    for i in data:
        if isinstance(data[i], dict):
            #print("It is a dict")
            outputDict(prefix + "." + i, data[i])
        else:
            if data[i] != None:
                writeGraphite(prefix + "." + i, data[i])

###############################
## START MAIN PROGRAM HERE
###############################

TOKEN = "37757c3e-eead-43b7-8193-b21bb99a6971"
api = screepsapi.API(token=TOKEN)

memoryData = api.memory(path="stats", shard="shard1")

s1 = json.dumps(memoryData)

memoryDict = json.loads(s1);

prefix = "screeps.official.shard1"

outputDict(prefix, memoryDict)
import screepsapi
import json
import os
import time
import pickle
import struct
import socket

def writeGraphite(prefix, value):
    cmdStr = "echo \"" + prefix + " " + str(value) + " `date +%s`\" | nc 127.0.0.1 2003"
    #print(prefix + ": " + str(value))
    #print(cmdStr)
    os.system(cmdStr)
    time.sleep(0.04)

def outputDict(prefix, data):
    for i in data:
        if isinstance(data[i], dict):
            #print("It is a dict")
            outputDict(prefix + "." + i, data[i])
        else:
            if data[i] != None:
                writeGraphite(prefix + "." + i, data[i])

def outputDictAsPickle(prefix, data):
    package = pickle.dumps(tuples, 1)
    size = struct.pack('!L', len(package))
    sock = socket.socket()
    sock.connect( ('127.0.0.1', 2004) )
    sock.sendall(size)
    sock.sendall(package)

###############################
## START MAIN PROGRAM HERE
###############################

TOKEN = "37757c3e-eead-43b7-8193-b21bb99a6971"
api = screepsapi.API(token=TOKEN)

while True:
    print(" ")
    print("Reading SHARD1....")
    memoryData = api.memory(path="stats", shard="shard1")

    s1 = json.dumps(memoryData)
    memoryDict = json.loads(s1);
    prefix = "screeps.official.shard1"
    outputDict(prefix, memoryDict)

    print("Reading SHARD2")
    memoryData = api.memory(path="stats", shard="shard2")

    s1 = json.dumps(memoryData)
    memoryDict = json.loads(s1);
    prefix = "screeps.official.shard2"
    outputDict(prefix, memoryDict)

    print("Sleeping....")
    time.sleep(60)
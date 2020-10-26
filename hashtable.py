members = [[123,"Robin","AB4"], [124,"Nguyen","HD12"], [125,"Jev","L18"], [126,"Will","OX5"], [127,"Lily","CH3"], [128,"Jonny","YO12"], [129,"Clara","BS1"], [130,"Callum","BA1"], [131,"Kirsten","SE2"]]
hashTable = []
for i in range(20):
    hashTable.append([i,[],[],[]])
def addMember(hashTable, members, currentMember, size):
    hashValue = ((members[currentMember][0])**2) % size
    foundAPlace = False
    i = 0
    while foundAPlace == False:
        if hashTable[hashValue][i] == []:
            hashTable[hashValue][i] = members[currentMember]
            foundAPlace = True
        else:
            i += 1
    return hashTable, print(members[currentMember][1], hashValue)
size = len(hashTable)
currentMember = 0
for currentMember in range(len(members)):
    addMember(hashTable, members, currentMember, size)
for i in range(len(hashTable)):
    print(hashTable[i])

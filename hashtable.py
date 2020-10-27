members = [[123,"Robin","AB4"], [124,"Nguyen","HD12"], [125,"Jev","L18"], [126,"Will","OX5"], [127,"Lily","CH3"], [128,"Jonny","YO12"], [129,"Clara","BS1"], [130,"Callum","BA1"], [131,"Kirsten","SE2"]]
hashPositions = {}
for i in range(len(members)):
    hashPositions[members[i][1]] = None
hashTable = []
for i in range(20):
    hashTable.append([i,[],[],[]])
def addMember(currentMember):
    hashValue = ((members[currentMember][0])**2) % size
    foundAPlace = False
    isDupe = True
    i = 0
    while foundAPlace == False:
        if members[currentMember] in hashTable[hashValue]:
            return print(members[currentMember][1], "is already in the table")
        else:
            isDupe = False
        if isDupe == False:
            if hashTable[hashValue][i] == []:
                hashTable[hashValue][i] = members[currentMember]
                hashPositions[members[currentMember][1]] = hashValue
                foundAPlace = True
            else:
                i += 1
    return hashTable, hashValue
def lookUpMember(name):
    position = None
    location = hashTable[hashPositions[name]]
    i = 1
    while position == None:
        if str(location[i][1]) == str(name):
            position = i
        i += 1
    return print(name, location[position])
def removeMember(name):
    hashTable
size = len(hashTable)
currentMember = 0
for currentMember in range(len(members)):
    addMember(currentMember)
for i in range(len(hashTable)):
    print(hashTable[i])
for i in range(len(members)):
    lookUpMember(members[i][1])
members.append([124,"Nguyen","HD12"])
lastMember = len(members)-1
addMember(lastMember)

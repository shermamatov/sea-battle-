import random
dots_area_arr = [['.','.','.','.','.','.','.'], ['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.']]
ships_coordinate = []
blocked_coordinate = []
def printBoard(arr):
    print("   " + "  ".join(str(i + 1) for i in range(len(arr[0]))))
    for i, row in enumerate(arr): print(chr(ord('A') + i) + "  " + "  ".join(row))

def shipNotBlockChecker(shipCoodinate):
    if(len(blocked_coordinate) != 0):
        for i in blocked_coordinate:
            if(shipCoodinate == i): 
                return False
            else: 
                return True
    else: 
        return True

def coordinateBlocker(coordinate):
    for i in coordinate:
        blocked_coordinate.append(i)
        if(i == 1):
            blocked_coordinate.append(2)
            blocked_coordinate.append(8)
            blocked_coordinate.append(9)
        elif(i == 7):
            blocked_coordinate.append(6)
            blocked_coordinate.append(13)
            blocked_coordinate.append(14)
        elif(i == 43):
            blocked_coordinate(36)
            blocked_coordinate(37)
            blocked_coordinate(44)
        elif(i == 49):
            blocked_coordinate(42)
            blocked_coordinate(48)
            blocked_coordinate(49)
        elif(1 < i < 7):
            blocked_coordinate.append(i - 1)
            blocked_coordinate.append(i + 1)
            blocked_coordinate.append(i + 7)
            blocked_coordinate.append(i + 6)
            blocked_coordinate.append(i + 8)
        elif( 43 < i < 49):
            blocked_coordinate.append(i + 1)
            blocked_coordinate.append(i - 1)
            blocked_coordinate.append(i - 6)
            blocked_coordinate.append(i - 7)
            blocked_coordinate.append(i - 8)
        elif(i % 7 == 0):
            blocked_coordinate.append(i - 1)
            blocked_coordinate.append(i - 7)
            blocked_coordinate.append(i + 7)
            blocked_coordinate.append(i + 6)
            blocked_coordinate.append(i - 8)
        elif((i + 1) % 7 == 0):
            blocked_coordinate.append(i + 1)
            blocked_coordinate.append(i + 7)
            blocked_coordinate.append(i - 7)
            blocked_coordinate.append(i - 6)
            blocked_coordinate.append(i + 8)
        else: 
            blocked_coordinate.append(i + 1)
            blocked_coordinate.append(i - 1)
            blocked_coordinate.append(i + 6)
            blocked_coordinate.append(i - 6)
            blocked_coordinate.append(i + 7)
            blocked_coordinate.append(i - 7)
            blocked_coordinate.append(i + 8)
            blocked_coordinate.append(i - 8)

def dispatcher(arr):
    for i in arr:
        ships_coordinate.append(i)
    coordinateBlocker(arr)
    # print(blocked_coordinate)

def ThreeShipsPlacer():
    firstRandom = random.randint(1, 49)
    shipArr = []
    if(firstRandom % 7 != 0 and (firstRandom - 1) % 7 != 0 and firstRandom != 1):
        shipArr.append(firstRandom)
        shipArr.append(firstRandom + 1)
        shipArr.append(firstRandom - 1)
        dispatcher(shipArr)
    elif (7 < firstRandom < 43):
        shipArr.append(firstRandom)
        shipArr.append(firstRandom - 7)
        shipArr.append(firstRandom + 7)
        dispatcher(shipArr)
    else:
        ThreeShipsPlacer()

def TwoShipsPlacer():
    firstRandom = random.randint(1, 49)
    shipArr = []
    if(shipNotBlockChecker(firstRandom)):
        if(firstRandom % 7 != 0 and shipNotBlockChecker(firstRandom + 1)):
            shipArr.append(firstRandom)
            shipArr.append(firstRandom + 1)
            dispatcher(shipArr)
        elif(firstRandom < 43 and shipNotBlockChecker(firstRandom + 7)):
            shipArr.append(firstRandom)
            shipArr.append(firstRandom + 7)
            dispatcher(shipArr)
        else:
            TwoShipsPlacer()
    else:
        TwoShipsPlacer()

def OneShipPlacer():
    firstRandom = random.randint(1, 49)
    if(shipNotBlockChecker(firstRandom)):
        dispatcher([firstRandom])
    else:
        OneShipPlacer()

ThreeShipsPlacer()
TwoShipsPlacer()
TwoShipsPlacer()
OneShipPlacer()
OneShipPlacer()
OneShipPlacer()
print(ships_coordinate)
import random
# player_name = input('enter your name: ')

dots_area_arr = [
        ['.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.']
]

ships_coordinate = []
blocked_coordinate = []

def printBoard(arr):
    print("   " + "  ".join(str(i + 1) for i in range(len(arr[0]))))
    for i, row in enumerate(arr):
        print(chr(ord('A') + i) + "  " + "  ".join(row))


def ThreeShipsPlacer():
    shipArr = []
    firstRandom = random.randint(1, 49)
    shipArr.append(firstRandom)
    
    print(shipArr)

ThreeShipsPlacer()


# printBoard(dots_area_arr)
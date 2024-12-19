def solveMaze(height, width, startCoords, endCoords, decrypted):
    determined = set()
    undetermined = []
    determinedPaths = set()
    undeterminedPaths = []
    maze = [[True for _ in range(width)] for _ in range(height)]
    numbers = []
    ind = 0
    while(ind < len(decrypted)):
        if(ind <= len(decrypted)-6 and decrypted[ind:ind+6] == "twenty"):
            numbers.append(20)
            ind += 6
        elif(ind <= len(decrypted)-8 and decrypted[ind:ind+8] == "nineteen"):
            numbers.append(19)
            ind += 8
        elif (ind <= len(decrypted) - 8 and decrypted[ind:ind + 8] == "eighteen"):
            numbers.append(18)
            ind += 8
        elif (ind <= len(decrypted) - 9 and decrypted[ind:ind + 9] == "seventeen"):
            numbers.append(17)
            ind += 9
        elif (ind <= len(decrypted) - 7 and decrypted[ind:ind + 7] == "sixteen"):
            numbers.append(16)
            ind += 7
        elif (ind <= len(decrypted) - 7 and decrypted[ind:ind + 7] == "fifteen"):
            numbers.append(15)
            ind += 7
        elif (ind <= len(decrypted) - 8 and decrypted[ind:ind + 8] == "fourteen"):
            numbers.append(14)
            ind += 8
        elif (ind <= len(decrypted) - 8 and decrypted[ind:ind + 8] == "thirteen"):
            numbers.append(13)
            ind += 8
        elif (ind <= len(decrypted) - 6 and decrypted[ind:ind + 6] == "twelve"):
            numbers.append(12)
            ind += 6
        elif (ind <= len(decrypted) - 6 and decrypted[ind:ind + 6] == "eleven"):
            numbers.append(11)
            ind += 6
        elif (ind <= len(decrypted) - 3 and decrypted[ind:ind + 3] == "ten"):
            numbers.append(10)
            ind += 3
        elif (ind <= len(decrypted) - 4 and decrypted[ind:ind + 4] == "nine"):
            numbers.append(9)
            ind += 4
        elif (ind <= len(decrypted) - 5 and decrypted[ind:ind + 5] == "eight"):
            numbers.append(8)
            ind += 5
        elif (ind <= len(decrypted) - 5 and decrypted[ind:ind + 5] == "seven"):
            numbers.append(7)
            ind += 5
        elif (ind <= len(decrypted) - 3 and decrypted[ind:ind + 3] == "six"):
            numbers.append(6)
            ind += 3
        elif (ind <= len(decrypted) - 4 and decrypted[ind:ind + 4] == "five"):
            numbers.append(5)
            ind += 4
        elif (ind <= len(decrypted) - 4 and decrypted[ind:ind + 4] == "four"):
            numbers.append(4)
            ind += 4
        elif (ind <= len(decrypted) - 5 and decrypted[ind:ind + 5] == "three"):
            numbers.append(3)
            ind += 5
        elif (ind <= len(decrypted) - 3 and decrypted[ind:ind + 3] == "two"):
            numbers.append(2)
            ind += 3
        elif (ind <= len(decrypted) - 3 and decrypted[ind:ind + 3] == "one"):
            numbers.append(1)
            ind += 3
        elif (ind <= len(decrypted) - 4 and decrypted[ind:ind + 4] == "zero"):
            numbers.append(0)
            ind += 4
    for i in range(len(numbers)//2):
        maze[numbers[2*i]][numbers[2*i+1]] = False

    undetermined.append((startCoords, 0,""))


    while undetermined:
        y = undetermined[0][0][0]
        x = undetermined[0][0][1]
        dist = undetermined[0][1]
        path = undetermined[0][2]
        if y != 0 and maze[y-1][x]:
            isDetermined = False
            for distances in determined:
                if distances[0] == (y-1,x):
                    isDetermined = True
            if not isDetermined:
                isUndetermined = False
                for distance in undetermined:
                    if distance[0] == (y-1,x):
                        isUndetermined = True
                        if dist + 1 < distance[1]:
                            undetermined.remove(distance)
                            undetermined.insert(binarySearch(dist + 1, undetermined, 0, len(undetermined)),((y-1,x),dist+1,path + "N"))
                        break
                if(not isUndetermined):
                    undetermined.insert(binarySearch(dist + 1, undetermined, 0, len(undetermined)),((y - 1, x), dist + 1, path + "N"))
        if x != 0 and maze[y][x-1]:
            isDetermined = False
            for distance in determined:
                if distance[0] == (y,x-1):
                    isDetermined = True
            if not isDetermined:
                isUndetermined = False
                for distance in undetermined:
                    if distance[0] == (y,x-1):
                        isUndetermined = True
                        if dist + 1 < distance[1]:
                            undetermined.remove(distance)
                            undetermined.insert(binarySearch(dist + 1, undetermined, 0, len(undetermined)),((y,x-1),dist+1,path + "W"))
                        break
                if(not isUndetermined):
                    undetermined.insert(binarySearch(dist + 1, undetermined, 0, len(undetermined)),((y, x-1), dist + 1,path + "W"))
        if y != len(maze)-1 and maze[y+1][x]:
            isDetermined = False
            for distance in determined:
                if distance[0] == (y+1,x):
                    isDetermined = True
            if not isDetermined:
                isUndetermined = False
                for distance in undetermined:
                    if distance[0] == (y+1,x):
                        isUndetermined = True
                        if dist + 1 < distance[1]:
                            undetermined.remove(distance)
                            undetermined.insert(binarySearch(dist + 1, undetermined, 0, len(undetermined)),((y+1,x),dist+1, path + "S"))
                        break
                if(not isUndetermined):
                    undetermined.insert(binarySearch(dist + 1, undetermined, 0, len(undetermined)),((y+1, x), dist + 1, path + "S"))
        if x != len(maze[0])-1 and maze[y][x+1]:
            isDetermined = False
            for distance in determined:
                if distance[0] == (y,x+1):
                    isDetermined = True
            if not isDetermined:
                isUndetermined = False
                for distance in undetermined:
                    if distance[0] == (y,x+1):
                        isUndetermined = True
                        if dist + 1 < distance[1]:
                            undetermined.remove(distance)
                            undetermined.insert(binarySearch(dist + 1, undetermined, 0, len(undetermined)),((y,x+1),dist+1, path + "E"))
                        break
                if(not isUndetermined):
                    undetermined.insert(binarySearch(dist + 1, undetermined, 0, len(undetermined)),((y, x+1), dist + 1, path + "E"))
        determined.add(undetermined[0])
        undetermined.pop(0)

    out = "Sir Odysseus, the paths to Troy are swarming with guards. There's no way in. (T＿T)"
    for distance in determined:
        if distance[0] == endCoords:
            out = distance[2]
    return out

def binarySearch(val, array, min, max):
    if min + 1== max:
        if val < array[min][1]:
            return min
        else:
            return min + 1
    middle = (min + max) // 2
    if val < array[middle][1]:
        return binarySearch(val, array, min, middle)
    else:
        return binarySearch(val, array, middle, max)



print(solveMaze(int(input()), int(input()), (0,0), (int(input()),int(input())), input()))
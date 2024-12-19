from collections import defaultdict
import math
import tkinter as tk
import random
from num2words import num2words

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

words = defaultdict(bool)
message = []

def decrypt(text, n, i, s, cur):
    global message
    print(text, i, s, cur)
    if message != []:
        return
    if i == n:
        if s == "":
            message.append(cur)
        return
    s += text[i]
    decrypt(text, n, i+1, s, cur)
    if words[s]:
        decrypt(text, n, i+1, "", cur+[s])

def decryptColumnar(text, tolerance):
    global words
    column = 1
    n = len(text)
    text = text.lower()
    while column <= n:
        cols = []
        length = math.ceil(n/column)
        rem = n%column
        ok = (rem == 0)
        cur = 0
        for _ in range(length):
            i = cur
            s = ""
            r = rem
            for _ in range(column):
                if i >= n:
                    break
                s += text[i]
                i += length
                if not ok and r == 0:
                    i -= 1
                else:
                    r -= 1
                if r == 0 and _ == column - 1:
                    break
            cur += 1
            cols.append(s)
        n = len(text)
        decrypt(''.join(cols), n, 0, "", [])
        column += 1


def main():
    global message
    #get words
    f = open("Words.txt", "r")
    for s in f:
        s = s.strip("\n")
        words[s] = True
    #remove weird words
    two_letters = ["is", "it", "as", "if", "or", "so", "to", "am", "an", "at", "do", "by", "go", "he"
        , "hi", "on", "of"]
    for i in range(ord('a'), ord('z') + 1):
        c = chr(i)
        if c != 'a' or c != 'i':
            for x in range(6):
                words[c*x] = False
        for j in range(ord('a'), ord('z') + 1):
            a = chr(i)
            b = chr(j)
            if a + b not in two_letters:
                words[a + b] = False

    words['a'] = True
    words['i'] = True

    numbers = ["ones", "twos", "threes", "fours", "fives", "sixs", "sevens", "eights", "nines"]
    for num in numbers:
        words[num] = False

    #decryption for columnar
    decryptColumnar("IPLIOZVZEA", 0)
    print(message)

    # Function to toggle the color of the button when clicked
    def toggle_color(row, col):
        if row == 0 and col == 0 or row == 9 and col == 9:
            return
        # Get the current color of the button
        current_color = grid_buttons[row][col]['bg']

        # Toggle the color between white and blue
        new_color = 'blue' if current_color == 'white' else 'white'

        # Use config to update the background color of the button
        grid_buttons[row][col].config(bg=new_color, highlightbackground=new_color)

        # Force the window to update the display
        root.update_idletasks()  # Ensure GUI updates after changing the button's color


    # Create the main window
    root = tk.Tk()
    root.title("Odysseus' Strategic Decoder")

    # Set the window size (make sure it's large enough to accommodate the grid)
    root.geometry("520x1200")

    # Create title label and place it at the top using grid
    title_label = tk.Label(root, text="Odysseus' Strategic Decoder", font=("Helvetica", 16, "bold"))
    title_label.grid(row=0, column=0, columnspan=20, pady=5)

    # Create text box for input and place it above the decrypt button
    decrypt_box = tk.Text(root, height=1, width=40)
    decrypt_box.grid(row=1, column=0, columnspan=20, pady=5)

    decrypt_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"))
    decrypt_label.grid(row=2, column=0, columnspan=20, pady=5)

    # Function for Decrypt (assuming `decryptColumnar` is defined somewhere)
    def get_decrypt():
        global message
        user_input = decrypt_box.get("1.0", "end-1c").strip("\n")
        message = []
        decryptColumnar(user_input, 0)
        print(message)
        if message:
            decrypt_label.config(text=" ".join(message[0]))

    # Create Decrypt button and place it below the text box
    decrypt_button = tk.Button(root, text="Get Decrypted Message", command = get_decrypt)
    decrypt_button.grid(row=3, column=0, columnspan=20, pady=5)

    # Create a label to display the encrypted message, placed above the "Get Encrypted Message" button
    encrypted_text_box = tk.Text(root, height=4, width=40, wrap="word", bg="lightgray")
    encrypted_text_box.grid(row=4, column=0, columnspan=20, pady=5)

    def generateEncryptedMessage():
        firstWord = ["Army", "Forces", "Troops", "Soldiers", "Legion"]
        thirdWord = ["located", "positioned", "situated", "placed", "lying"]
        i = 0
        j = 0
        while(True):
            i, j = random.randint(0, 9), random.randint(0, 9)
            if i == 0 and j == 0 or i == 9 or j == 9:
                continue
            break
        i = num2words(i)
        j = num2words(j)
        message = firstWord[random.randint(0, 4)] + " is " + thirdWord[random.randint(0, 4)] + " at " + str(
            i) + " " + str(j)
        print(message)
        columns = random.randint(2, 10)
        cols = ["" for _ in range(columns)]
        cur = 0
        message = message.replace(" ", "")
        print(message)
        n = len(message)
        for c in message:
            cols[cur] += c
            cur += 1
            cur %= columns
            n -= 1
            if n == 0:
                break
        s = ''.join(cols)
        encrypted_text_box.delete(1.0, tk.END)  # Delete previous content (if any)
        encrypted_text_box.insert(tk.END, s)

        # Force the window to update the display
        root.update_idletasks()

    # Create Encrypt button and place it below the Encrypted Message label
    encrypt_button = tk.Button(root, text="Get Encrypted Message", command=generateEncryptedMessage)
    encrypt_button.grid(row=5, column=0, columnspan=20, pady=5)

    coors_text_box = tk.Text(root, height=4, width=40, wrap="word", bg="lightgray")
    coors_text_box.grid(row=6, column=0, columnspan=20, pady=5)

    # Initialize a 2D list to store button references for the grid
    grid_buttons = []

    def getPath():
        coors = coors_text_box.get("1.0", "end-1c").strip("\n")
        print(coors)
        ans = solveMaze(10, 10, (0,0), (9,9), coors)
        ans_label.config(text = "Path: " + ans + " Length: " + str(len(ans)))


    path_button = tk.Button(root, text="Get Shortest Path", command=getPath)
    path_button.grid(row=7, column=0, columnspan=20, pady=5)

    ans_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"))
    ans_label.grid(row=8, column=0, columnspan=20, pady=5)

    # Create a 20x20 grid of buttons
    for row in range(10):
        grid_buttons.append([])  # Add a new row to the list
        for col in range(10):
            # Create a button for each square in the grid
            button = tk.Button(root, width=1, height=1, bg='white',
                               highlightbackground='white',  # Set initial highlight color
                               command=lambda r=row, c=col: toggle_color(r, c))

            # Place the button in the grid using grid()
            button.grid(row=row + 9, column=col, padx=1, pady=1)  # Adjust row to start after text box and buttons

            # Store the reference to the button in the list
            grid_buttons[row].append(button)

    grid_buttons[0][0].config(bg="green", highlightbackground="green")
    grid_buttons[-1][-1].config(bg="red", highlightbackground="red")

    root.mainloop()

if __name__ == "__main__":
    main()

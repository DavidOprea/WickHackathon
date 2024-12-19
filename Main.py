from collections import defaultdict
import math
import tkinter as tk
import random
from num2words import num2words

words = defaultdict(bool)
message = []

def decrypt(text, i, s, cur):
    global message
    print(text, i, s, cur)
    if message != []:
        return
    if i == len(text):
        if s == "":
            message.append(cur)
        return
    s += text[i]
    decrypt(text, i+1, s, cur)
    if words[s]:
        decrypt(text, i+1, "", cur+[s])

def generateEncryptedMessage():
    firstWord = ["Army", "Forces", "Troops", "Soldiers", "Legion"]
    thirdWord = ["located", "positioned", "situated", "placed", "lying"]
    i, j = random.randint(0, 19), random.randint(0, 19)
    i = num2words(i)
    j = num2words(j)
    message = firstWord[random.randint(0, 4)] + " is " + thirdWord[random.randint(0, 4)] + " at " + str(i) + " " + str(j)
    print(message)
    columns = random.randint(2, 10)
    cols = ["" for _ in range(columns)]
    cur = 0
    message = message.replace(" ", "")
    for c in message:
        cols[cur] += c
        cur += 1
        cur %= columns
    print(cols)
    print(''.join(cols))

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
            cur += 1
            cols.append(s)
        decrypt(''.join(cols), 0, "", [])
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

    #decryption for columnar
    decryptColumnar("IPLIOZVZEA", 0)
    print(message)
    generateEncryptedMessage()

    # Create the main window
    root = tk.Tk()
    root.title("Odysseus' Strategic Decoder")

    # Set the window size
    root.geometry("1000x1000")

    title_label = tk.Label(root, text="Odysseus' Strategic Decoder", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=20)

    def get_decrypt():
        global message
        user_input = decrypt_box.get("1.0", "end-1c").strip("\n")
        message = []
        decryptColumnar(user_input, 0)
        print(user_input)
        print(message)

    #Create text box
    decrypt_box = tk.Text(root, height=10, width=40)
    decrypt_box.pack(pady=20)


    decrypt_button = tk.Button(root, text="Get Decrypted Message", command=get_decrypt)
    decrypt_button.pack()

    encrypt_button = tk.Button(root, text="Get Encrypted Message", command=generateEncryptedMessage)
    encrypt_button.pack()

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()

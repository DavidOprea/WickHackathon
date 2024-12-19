from collections import defaultdict

words = defaultdict(bool)

def decryptColumnar(text, tolerance):
    global words
    column = 1
    n = len(text)
    while True:
        cols = []
        length = n//column
        rem = n % column
        cur = 0
        for _ in range(column):
            i = cur
            add = 0
            if rem != 0:
                add = 1
            for _ in range()
            if rem != 0:
                cols.append(text[cur:cur+length+1])
                cur += 1
                rem -= 1
            else:
                cols.append(text[cur:cur+length])
                cur += length
        print(cols)
        if column == 2:
            break
        column += 1


def main():
    decryptColumnar("HLOEL", 0)

if __name__ == "__main__":
    main()

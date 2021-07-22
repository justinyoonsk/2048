board = [[0, 0, 2, 2], [2, 2, 16, 0], [4, 0, 0, 4], [0, 2, 0, 0]]

def display():
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element


    for row in board:
        currRow = "|"
        for element in row:
            if element == 0:
                currRow += " |"
            else:
                currRow += str(element) + "|"

        print(currRow)
    print()

display()


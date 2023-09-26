

from random import randint


#Board for holding ship locations
HIDDEN_BOARD = [[" "] * 25 for x in range(25)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 25 for i in range(25)]

def print_board(board):
    print("  A B C D E F G H I J K L M N O P Q R S T U V W X Y")
    print("  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24

}
#computer create 5 ships
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,24), randint(0,24)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"

def get_ship_location():
    row = input("choose any row. Hint: type any digit 1-25: ").upper()
    while row not in "12345678910111213141516171819202122232425":
        print('That does not work, try something else')
        row = input("choose any row. Hint: type any digit 1-25: ").upper()
    column = input("now choose any column Hint: type a letter A-Y: ").upper()
    while column not in "ABCDEFGHIJKLMNOPQRSTUVWXY":
        print('That does not work, try something else')
        column = input("now choose any column. Hint: type a letter A-Y: ").upper()
    return int(row) - 1, letters_to_numbers[column]

#check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

if __name__ == "__main__":
    create_ships(HIDDEN_BOARD)
    turns = 60
    while turns > 0:
        print('Guess the coordinates of the battleship')
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "~":
            print("You already guessed there, try agian.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("HIT!")
            GUESS_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("Miss.")
            GUESS_BOARD[row][column] = "~"
            turns -= 1
        if count_hit_ships(GUESS_BOARD) == 3:
            print("You have achieved a VICTORY!")
            break
        print("You have " + str(turns) + " turns remaining")
        if turns == 0:
            print("SORRY! You have run out of turns")

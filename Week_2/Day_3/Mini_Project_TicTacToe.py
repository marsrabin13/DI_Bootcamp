'''Tic Tac Toe: A command-line Tic Tac Toe game that allows two players to take turns marking a 3x3 grid.'''
print("Welcome to TIC TAC TOE!")
#initial grid
tictac_grid = [[" "] * 3 for _ in range(3)]
winner_found = False
game_tie = False

def display_board():
    print("TIC TAC TOE")
    print("*"*13)
    for index,row in enumerate(tictac_grid):
        print("* " + " | ".join(row) + " *")
        if index < 2:
            print("*"+"-"*3 + "|" + "-"*3 + "|"+ "-"*3 +"*")
    print("*"*13)


def player_input(player):
    print(f"Player {player}'s turn, input your answer:")
    while True:
        try:
            row = int(input("Enter Row: "))
            col = int(input("Enter Column: "))
            if tictac_grid[row-1][col-1] == " ":
                tictac_grid[row-1][col-1] = player
                display_board()
                break
            else:
                print("Invalid! Choose anoter spot. try again!")
        except ValueError:
            print("Invalid! Enter only numbers. try again!")
        except IndexError:
            print("Invalid! Enter numbers between 1-3 ,try again!")

def check_win():
    #check rows
    for row in tictac_grid:
        if len(set(row)) == 1 and set(row) != {" "}:
            return True

    #check columns
    for col in range(len(tictac_grid)):
        column = []
        for row in range(len(tictac_grid)):
            column.append(tictac_grid[row][col])
        if len(set(column)) == 1 and set(column) != {" "}:
            return True

    #check diagonal
    diagonal1 = [tictac_grid[i][i] for i in range(3)]
    if len(set(diagonal1)) == 1 and set(diagonal1) != {" "}:
        return True

    #check opposite diagonal
    diagonal2 = [tictac_grid[i][2-i] for i in range(3)]
    if len(set(diagonal2)) == 1 and set(diagonal2) != {" "}:
        return True
    
    return False

def is_board_full():
    for row in tictac_grid:
        for col in row:
            if col == " ":
                return False
    return True


            
def check_tie():

    if check_win() == False and is_board_full() == True:
        return True
    else:
        return False

def play():
    winner_found = False
    game_tie = False
    players = ["O","X"]
    while winner_found == False and game_tie == False:
        display_board()
        #if is_board_full() == True:


        for player in players: 
            player_input(player)
            winner_found = check_win()
            if winner_found == True:
                print(f"Player {player} won!!!")
                break

            game_tie = check_tie()
            if game_tie == True:
                print("it's a tie!")
                break

play()
    

            












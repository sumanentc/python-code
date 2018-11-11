#from IPython.display import clear_output
import random


def player_input():
    marker= ' '
    while(marker != 'X' or marker!='O'):
        marker=input("Player 1 Choose X or O: ").upper();
        if(marker=='X'):
            return ('X','O')
        else:
            return ('O','X')

def display_board(board):
    #clear_output()
    print('\n'*100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("-|-|-");
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-|-|-");
    print(board[1] + '|' + board[2] + '|' + board[3])

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,marker):

    return (
    (board[1] == board[2] == board[3] == marker) or #ROW check
    (board[4] == board[5] == board[6] == marker) or #ROW check
    (board[7] == board[8] == board[9] == marker) or #ROW check
    (board[7] == board[4] == board[1] == marker) or #Column check
    (board[8] == board[5] == board[2] == marker) or #Column check
    (board[9] == board[6] == board[3] == marker) or #Column check
    (board[7] == board[5] == board[3] == marker) or
    (board[9] == board[5] == board[1] == marker)
            )

def choose_first():
    flip = random.randint(0,1)
    if flip ==0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board,position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if(space_check(board,i)):
            return False

    return True;
def player_choice(board,player):
    position=0
    while(position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position)):
        position = int(input(player + " Choose Position :(1-9): "))
    return position
def replay():
    choice = input("Do you want to play : Enter Yes or No ")
    return choice.lower()=='yes'

print("Welcome To Tic Tac Toe!!!!")

while True:
    # PLAY the Game
    the_board=[' ']*10;
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first")
    play_game= input("Ready to play Y or N ?")
    if(play_game=='Y'):
        game_on=True
    else:
        game_on=False

    while(game_on):
        if(turn =='Player 1'):
            display_board(the_board)
            position = player_choice(the_board,turn)
            place_marker(the_board,player1_marker,position)
            if(win_check(the_board,player1_marker)):
                display_board(the_board)
                print("Player 1 has won !")
                game_on=False;
            else:
                if (full_board_check(the_board)):
                    display_board(the_board)
                    print("Game is Tie !!")
                    game_on = False;
                else:
                    turn='Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board,turn)
            place_marker(the_board, player2_marker, position)
            if (win_check(the_board, player2_marker)):
                display_board(the_board)
                print("Player 2 has won !")
                game_on = False;
            else:
                if (full_board_check(the_board)):
                    display_board(the_board)
                    print("Game is Tie !!")
                    game_on = False;
                else:
                    turn = 'Player 1'



    if not replay():
        break;









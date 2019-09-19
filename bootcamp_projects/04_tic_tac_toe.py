import sys

def create_board():
    board = ['#']
    for num in range(1,10):
        board.append(' ')
    return board


def display_board(board):
    for num1 in range(1,4):
        print(board[num1]),
        if num1 == 3:
            continue
        print('|'),
    print('')
    print('----------')

    for num2 in range(4,7):
        print(board[num2]),
        if num2 == 6:
            continue
        print('|'),
    print('')
    print('----------')

    for num3 in range(7, 10):
        print(board[num3]),
        if num3 == 9:
            continue
        print('|'),
    print('')


def help_board():
    num_board = ['#']
    for num in range(1, 10):
        num_board.append(num)
    print('Here are the numbers for positioning:')
    display_board(num_board)
    print('')


def player_symbols():
    player_one = raw_input('Player one: What do you want your symbol to be? ')
    player_two = raw_input('Player two: What do you want your symbol to be? ')
    while player_one == player_two:
        print('You both can\'t have the same symbol.')
        player_one = raw_input('Player one: What do you want your symbol to be? ')
        player_two = raw_input('Player two: What do you want your symbol to be? ')
    return player_one, player_two


def update_board(board, player):
    """ Updates board with player character
        Gets the location and the player char and places it on the board unless already taken

        Args:
            board: an array for the board contianing the positions of the players
            player: a character that represents the player

        Returns:
            A board with the newly added player position
    """
    while True:
        try:
            position = int(input('Player %s where do you want to place your marker? ' % player))
            if position not in range(1,10):
                raise
            while board[position] != ' ':
                position = int(input('That position is already taken, try another. '))
                if position not in range(1, 10):
                    raise
            break
        except (KeyboardInterrupt, SystemExit):
            sys.exit()
        except:
            print('Value must be 1-9, inclusive.')

    board[position] = player
    print('')
    print('')
    return board


def check_won(board,player):
    """ Checks if a player won
        Checks x,y and diagonals for matching characters. Excludes blank space\

        Args:
            board: an array for the board contianing the positions of the players
            player: a character that represents the player

        Returns:
            A boolean depending if a player won
    """
    # X axis
    if (
        (len(set(board[1:4])) == 1 and ' ' not in set(board[1:4])) or
        (len(set(board[4:7])) == 1 and ' ' not in set(board[4:7])) or
        (len(set(board[7:10])) == 1 and ' ' not in set(board[7:10]))
    ):
        print('Player %s, you win!' % player)
        display_board(board)
        return True
    # Y axis
    if (
        (len(set(board[1::3])) == 1 and ' ' not in set(board[1::3])) or
        (len(set(board[2::3])) == 1 and ' ' not in set(board[2::3])) or
        (len(set(board[3::3])) == 1 and ' ' not in set(board[3::3]))
    ):
        print('Player %s, you win!' % player)
        display_board(board)
        return True
    # Diagonals
    if (
        (len(set(board[1::4])) == 1 and ' ' not in set(board[1::4])) or
        (len(set(board[3:9:2])) == 1 and ' ' not in set(board[3:9:2]))
    ):
        print('Player %s, you win!' % player)
        display_board(board)
        return True

    return False


def check_board_full(board):
    if ' ' in board:
        return False
    print('It\'s a draw')
    display_board(board)
    return True


game_over = False
play_again = True
while play_again == True:
    game_board = create_board()
    players = player_symbols()
    help_board()
    while game_over == False:
        print('Player one\'s turn.')
        display_board(game_board)
        update_board(game_board, players[0])
        game_over = check_won(game_board, players[0])
        if game_over == True:
            break
        game_over = check_board_full(game_board)
        if game_over == True:
            break

        print('Player two\'s turn.')
        display_board(game_board)
        update_board(game_board, players[1])
        game_over = check_won(game_board, players[1])
        if game_over == True:
            break
        game_over = check_board_full(game_board)

    if raw_input('Want to play again,\'yes\'? ').lower().startswith('y') == 'yes':
        play_again = True
        game_over = False
    else:
        play_again = False
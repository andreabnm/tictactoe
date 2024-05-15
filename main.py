board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


def draw_board():
    for x in range(3):
        print('----------------')
        line = ''
        for y in range(3):
            value = board[x][y]

            if y == 0:
                line += '  ' + value
            else:
                line += '  |  ' + value
        print(line)


def choose_new_position(current_symbol):
    new_x = ''
    while not new_x.isnumeric():
        new_x = input(f'{current_symbol}: choose horizontal position [1 - 3]: ')
        if not new_x.isnumeric():
            new_x = ''
        else:
            if not (1 <= int(new_x) <= 3):
                new_x = ''
    new_y = ''
    while not new_y.isnumeric():
        new_y = input(f'{current_symbol}: choose vertical position [1 - 3]: ')
        if not new_y.isnumeric():
            new_y = ''
        else:
            if not (1 <= int(new_y) <= 3):
                new_y = ''

    return int(new_x), int(new_y)


def is_game_over(curr_symbol):
    if curr_symbol == '':
        return False
    # The game is over when the current symbol forms a line (current_symbol is winner)
    # or when on the board there are not positions left (tie)

    if (board[0][0] == board[0][1] == board[0][2] == curr_symbol) or \
            (board[1][0] == board[1][1] == board[1][2] == curr_symbol) or \
            (board[2][0] == board[2][1] == board[2][2] == curr_symbol) or \
            (board[0][0] == board[1][1] == board[2][2] == curr_symbol) or \
            (board[2][0] == board[1][1] == board[0][2] == curr_symbol) or \
            (board[0][0] == board[1][0] == board[2][0] == curr_symbol) or \
            (board[0][1] == board[1][1] == board[2][1] == curr_symbol) or \
            (board[0][2] == board[1][2] == board[2][2] == curr_symbol):
        print(f'{curr_symbol} WINS!')
        return True

    # Check if tie
    tie = True
    for x in range(3):
        for y in range(3):
            if board[x][y] == ' ':
                tie = False
    if tie:
        print('TIE!')
        return True
    return False


def main():
    continue_game = True
    x_turn = True
    symbol = ''

    while continue_game:
        draw_board()
        continue_game = not is_game_over(symbol)
        if continue_game:
            symbol = 'X' if x_turn else 'O'
            valid_position = False
            new_x, new_y = 0, 0

            while not valid_position:
                new_x, new_y = choose_new_position(symbol)
                if board[new_x - 1][new_y - 1] != ' ':
                    print(f'Position {new_x},{new_y} already taken, please select another one.')
                else:
                    valid_position = True

            board[new_x - 1][new_y - 1] = symbol
            x_turn = not x_turn


if __name__ == '__main__':
    main()

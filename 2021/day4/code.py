import copy

def read_file():
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file]
    return lines


def get_input(lines):
    draw = [int(n) for n in lines[0].split(",")]
    boards = []     # 3D array containing all boards (2D array)
    index = -1      # index of the current board
    for row in range(1, len(lines)):
        if row % 6 == 1:    # the empty row before first number row
            boards.append([])
            index += 1
        else:               # number rows of current board
            boards[index].append([int(n) for n in lines[row].split()])
    return draw, boards


def check_hor(numbs, board):
    for row in board:
        for col in range(0, len(row)):
            if row[col] not in numbs:
                break
            elif col == len(row)-1:
                return True
    return False


def check_ver(numbs, board):
    for col in range(0, len(board[0])):
        for row in range(0, len(board)):
            if board[row][col] not in numbs:
                break
            elif row == len(board)-1:
                return True
    return False


def check_bingo(numbs, board):
    return check_hor(numbs, board) or check_ver(numbs, board)


def find_bingo(numbs, boards):
    for ind in range(0, len(boards)):
        if check_bingo(numbs, boards[ind]):
            return ind
    return -1   # no bingo


def calc_unmarked(numbs, board):
    usum = 0
    for row in board:
        for val in row:
            if val not in numbs:
                usum += val
    return usum


def part1():
    draw, boards = get_input(read_file())
    i = 5
    winner = find_bingo(draw[:i], boards)
    while(winner == -1):
        i += 1
        winner = find_bingo(draw[:i], boards)
    last_called = draw[i-1]     # the last number called before bingo
    unsum = calc_unmarked(draw[:i], boards[winner])
    print(last_called * unsum)


def part2():
    draw, boards = get_input(read_file())
    last_winner = None
    last_called = -1
    for i in range(4, len(draw)):
        if len(boards) > 0:
            winner = find_bingo(draw[:i], boards)
            while winner != -1:
                last_winner = boards.pop(winner)
                last_called = i
                winner = find_bingo(draw[:i], boards)
    unsum = calc_unmarked(draw[:last_called], last_winner)
    print(draw[last_called-1], unsum)
    print(draw[last_called-1] * unsum)


if __name__ == '__main__':
#    part1()
    part2()

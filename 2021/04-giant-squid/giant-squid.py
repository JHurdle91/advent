import numpy as np


def giant_squid(file_in):
    nums, boards = process_input(file_in)
    trackers = [[[0 for i in range(5)] for j in range(5)] for k in range(len(boards))]
    winners = [0] * len(boards)
    last_board = False
    for num in nums:
        i = 0
        if sum(winners) == 99:
            loser_index = winners.index(0)
            last_board = True
        for board in boards:
            if winners[i] == 1:
                i += 1
                continue
            tracker, hit = check_board(board, num, trackers[i])
            if hit:
                trackers[i] = tracker
                if isWinner(tracker):
                    winners[i] = 1
                    if last_board:
                        getScore(board, tracker, num)
                        return
            i += 1

def check_board(board, num, tracker):
    for i in range(len(board)):
        n = str(num)
        if n in board[i]:
            j = board[i].index(n)
            tracker[i][j] = 1
            return tracker, True
    return tracker, False

def isWinner(tracker):
    right_diag = 0
    left_diag = 0
    for i in range(5):
        if sum(tracker[i]) == 5:
            return True

        col_sum = 0
        for j in range(5):
            col_sum += tracker[j][i]
        if col_sum == 5:
            return True

        right_diag += tracker[i][i]
        left_diag += tracker[i][-i]
    if right_diag == 5 or left_diag == 5:
        return True
    return False

def getScore(board, tracker, num):
    mask = np.ma.masked_where(tracker, board)
    masked = np.ma.compressed(mask)
    score = 0
    for item in masked:
        score += int(item)
    score *= int(num)
    print(score)

def process_input(file_in):
    with open(file_in) as f:
        lines = f.read().splitlines()
    nums = lines[0].split(',')
    boards = []
    j = -1
    for i in range(1, len(lines)):
        if lines[i] == "":
            boards.append([])
            j += 1
            continue
        boards[j].append(lines[i].strip().replace('  ', ' ').split(' '))
    return nums, boards


giant_squid('input.txt')

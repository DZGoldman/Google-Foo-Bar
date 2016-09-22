'''
There you have it. Yet another pointless "bored" game created by the bored minions of Professor Boolean.
The game is a single player game, played on a board with n squares in a horizontal row. The minion places a token on the left-most square and rolls a special three-sided die.
If the die rolls a "Left", the minion moves the token to a square one space to the left of where it is currently. If there is no square to the left, the game is invalid, and you start again.
If the die rolls a "Stay", the token stays where it is.
If the die rolls a "Right", the minion moves the token to a square, one space to the right of where it is currently. If there is no square to the right, the game is invalid and you start again.
The aim is to roll the dice exactly t times, and be at the rightmost square on the last roll. If you land on the rightmost square before t rolls are done then the only valid dice roll is to roll a "Stay". If you roll anything else, the game is invalid (i.e., you cannot move left or right from the rightmost square).
To make it more interesting, the minions have leaderboards (one for each n,t pair) where each minion submits the game he just played: the sequence of dice rolls. If some minion has already submitted the exact same sequence, they cannot submit a new entry, so the entries in the leader-board correspond to unique games playable.
Since the minions refresh the leaderboards frequently on their mobile devices, as an infiltrating hacker, you are interested in knowing the maximum possible size a leaderboard can have.
Write a function answer(t, n), which given the number of dice rolls t, and the number of squares in the board n, returns the possible number of unique games modulo 123454321. i.e. if the total number is S, then return the remainder upon dividing S by 123454321, the remainder should be an integer between 0 and 123454320 (inclusive).
n and t will be positive integers, no more than 1000. n will be at least 2.
'''


def answer(t, n):
    # Initiate dictionary for memoization of all game cells visited:
    all_visited_cells = {}
    def get_path_count(current_position, moves_left):
        # if we're at the end of the board, record as win
        if current_position == n - 1:
            return 1
        # If we precede the first cell, or don't have enough moves to get to the end, record as loss:
        elif current_position < 0 or moves_left < (n - 1) - current_position:
            return 0
        #For optimization, if we have exactly the right number of moves left, record as win
        elif moves_left == n - 1 - current_position:
            return 1
        # If it isn't a win or a loss...
        else:
            # See if upcoming move has been made already
            moves_left -= 1
            status = str((current_position,moves_left))
            # If it has, return path count of this move
            if status in all_visited_cells:
                return all_visited_cells[status]
            # Otherwise, make all three possible moves and record the move in all_visited_cells
            else:
                number = (get_path_count(current_position - 1, moves_left) +\
                get_path_count(current_position, moves_left) +\
                get_path_count(current_position + 1, moves_left)) % 123454321
                # put it in the paths
                all_visited_cells[status] = number
                return number
    # Initiate recursive algorithm:
    return get_path_count(current_position=0, moves_left=t)

print(
    # panswer(10,4)
)

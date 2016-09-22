'''
Write a function answer(food, grid) that returns the number of units of food Beta Rabbit will have at the end, given that he takes a route using up as much food as possible without him being eaten, and ends at the bottom right room. If there does not exist a route in which Beta Rabbit will not be eaten, then return -1.

food is the amount of food Beta Rabbit starts with, and will be a positive integer no larger than 200.

grid will be a list of N elements. Each element of grid will itself be a list of N integers each, denoting a single row of N rooms. The first element of grid will be the list denoting the top row, the second element will be the list denoting second row from the top, and so on until the last element, which is the list denoting the bottom row. In the list denoting a single row, the first element will be the amount of food the zombie in the left-most room in that row needs, the second element will be the amount the zombie in the room to its immediate right needs and so on. The top left room will always contain the integer 0, to indicate that there is no zombie there.

The number of rows N will not exceed 20, and the amount of food each zombie requires will be a positive integer not exceeding 10.
'''


def answer (food, grid):
    # method: breadth first, starting with final room, working backward. Tracks all possible paths and passes them forward until it reaches first room
    class Room:
        def __init__(self, row, column, food ):
            self.row = row
            self.column = column
            self.food = food
            self.paths = set()
            self.current = False
    r = range(len(grid))
    # Maze mirrors grid but with Room instantiations instead of just numbers
    maze = [[Room(row = row, column = col, food = grid[row][col]) for col in r] for row in r]
    # set starting room:
    maze[-1][-1].current = True
    maze[-1][-1].paths.add(0)
    # Helper funciton: find all current rooms
    def current_rooms():
        return [room for row in maze for room in row if room.current ]
    # run update block 2*n-1 times
    for _ in range(2*(len(maze)-1)):
        # Update: add food to paths in current room, find next rooms, combine paths and set as current for next iteration
        for room in current_rooms():
            # add food in room to rooms paths
            room.paths = set([n + room.food for n in list(room.paths)])
            room.current = False
            # find next rooms
            if room.row > 0:
                new_room = maze[room.row - 1][room.column]
                new_room.current = True
                # comine paths
                new_room.paths |= room.paths
            if room.column > 0:
                new_room = maze[room.row][room.column - 1]
                new_room.current = True
                new_room.paths |= room.paths

    all_paths = list(maze[0][0].paths)
    # find max path less than food limit
    solution = -1
    for num in all_paths:
        if  solution < num <=food:
            solution = num
    return food - solution if not solution==-1 else solution

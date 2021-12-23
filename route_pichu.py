
#
# Submitted by : [UJWALA MUSKU AND ujmusku@iu.edu HERE]
#
# Based on skeleton code in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
    return 0 <= pos[0] < n and 0 <= pos[1] < m

#Possible moves from a position
def moves(map, row, col, visited_positions):
    moves = ((row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1))
    # Return only moves that are within the house_map and legal (i.e. go through open space "." and not in already visited positions)
    # Introducing a list that consists of already visited positions in the previous successors. This visited list helps the code in making sure that we
    # don't keep repeating the same path i.e., indefinite loop.
    return [move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@") and (move[0],move[1]) not in visited_positions]

# Adding a path to a
def add_path(fringe,move,curr_dist):
    new_list = fringe[0].copy()
    new_thing = (move, curr_dist + 1)
    new_list.append(new_thing)
    return new_list

# Function that searches the house map with above restrictions of following valid indexing, choosing better successors (moves function above)
def search(house_map):
    # Find pichu start position before searching the destination(@)
    pichu_loc = [(row_i, col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i] == "p"][0]
    fringe = [[(pichu_loc, 0)]]
    #Saving once visited positions into a list(visited_positions) to avoid indefinite loop
    visited_positions = [pichu_loc]
    while fringe:
        (curr_move, curr_dist) = fringe[0][-1]
        # From the current position, we iterate over each possible move(successor) and check if we reach the destination.
        # Once we reach the destination, we break the loop because we already have a path in place.
        # If we didn't reach the destination yet, we keep add that path into the fringe so that we store the path
        # We keep doing this untill the fringe is empty with no paths left.
        for move in moves(house_map, *curr_move, visited_positions):
            visited_positions.append(move)
            if house_map[move[0]][move[1]] == "@":
                #print("Yayy")
                steps, final_path = path_solution(add_path(fringe,move,curr_dist))
                return steps, final_path
                break
            else:
                fringe.append(add_path(fringe,move,curr_dist))
        # Once we check the first element(which is essentially a path) in a fringe above and appending the new successor to
        # the fringe, we pop the first element because we already got the possible successors and path in place.
        fringe.pop(0)

# This function returns the path in terms of L,R,U, and D from one position in the matrix to another position.
def path_solution(sol_list):
    path_value = ""
    #Returning -1 when there is no solution for a particular input matrix house map
    if sol_list is None:
        return -1," "
    else:
        for i in range(1, len(sol_list)):
            #Downward movement
            if (sol_list[i][0][0] - sol_list[i - 1][0][0] == 1):
                # print("D")
                path_value += 'D'
            #Upward movement
            elif (sol_list[i - 1][0][0] - sol_list[i][0][0] == 1):
                # print("U")
                path_value += 'U'
            #Right movement
            elif (sol_list[i][0][1] - sol_list[i - 1][0][1] == 1):
                # print("R")
                path_value += 'R'
            #Left movement
            elif sol_list[i - 1][0][1] - sol_list[i][0][1] == 1:
                # print("L")
                path_value += 'L'
        return sol_list[-1][1],path_value


#This is the main function that uses the above defined initial,goal and successor functions to come up with shortest path and number of steps
if __name__ == "__main__":
    #house_map = parse_map(str(sys.argv[0]).split("/venv")[0]+"/map1.txt")
    house_map = parse_map(str(sys.argv[1]))
    print("Shhhh... quiet while I navigate!")
    #solution = search(house_map)
    #steps, final_path = path_solution(solution)
    steps, final_path = search(house_map)
    print("Here's the solution I found:")
    print(steps,final_path)

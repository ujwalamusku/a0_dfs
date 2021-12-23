
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [UJWALA MUSKU AND ujmusku@iu.edu HERE]
#
# Based on skeleton code in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    #if agent_condition(house_map,row,col) is True and house_map[row][col] == ".":
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ])

# The following four functions check the four different directions of a diagonal(right diagonal and left diagonal)
# These four functions check the position of "p" first and if "p" is present, it looks for "X" or "@" in between "p"th position
# and expected new "p"th insertion position.
# This function checks the lower part of the left diagonal( which is essentially the right bottom part of two diagonals intersecting to each other)
# Checks the position by increasing both row and column by 1
def right_bottom_diagonal(house_map,r,c):
    in_r, in_c = r, c
    while r in range(0, len(house_map)) and c in range(0, len(house_map[0])):
        if house_map[r][c] == "p":
            (p_row, p_col) = (r, c)
            while r in range(0, p_row + 1) and c in range(0, p_col + 1):
                if house_map[r - 1][c - 1] not in ("X", "@"):
                    r -= 1
                    c -= 1
                    if r <= in_r or c <= in_c:
                        return False
                else:
                    break
            break
        else:
            r += 1
            c += 1

# This function checks the upper part of the left diagonal( which is essentially the left top part of two diagonals intersecting to each other)
# Checks the position by reducing the row and column index by 1
def left_top_diagonal(house_map,r,c):
    in_r,in_c = r,c
    while r in range(0, len(house_map)) and c in range(0, len(house_map[0])):
        if house_map[r][c] == "p":
            (p_row, p_col) = (r, c)
            while r in range(p_row, in_r) and c in range(p_col, in_c):
                if house_map[r + 1][c + 1] not in ("X", "@"):
                    r += 1
                    c += 1
                    if r >= in_r or c >= in_c:
                        return False
                else:
                    break
            break
        else:
            r -= 1
            c -= 1

# This function checks the lower part of the right diagonal( which is essentially the left bottom part of two diagonals intersecting to each other)
# Checks the position by increasing row by 1 and reducing column by 1
def left_bottom_diagonal(house_map,r,c):
    in_r,in_c = r,c
    while r in range(0, len(house_map)) and c in range(0, len(house_map[0])):
        if house_map[r][c] == "p":
            (p_row, p_col) = (r, c)
            while r in range(in_r, p_row + 1) and c in range(p_col, in_c):
                if house_map[r - 1][c + 1] not in ("X", "@"):
                    r -= 1
                    c += 1
                    if r <= in_r or c >= in_c:
                        return False
                else:
                    break
            break
        else:
            r += 1
            c -= 1

# This function checks the top part of the right diagonal( which is essentially the right top part of two diagonals intersecting to each other)
# Checks the position by reducing row index by 1 and increasing column index by 1
def right_top_diagonal(house_map,r,c):
    in_r,in_c = r,c
    while r in range(0, len(house_map)) and c in range(0, len(house_map[0])):
        if house_map[r][c] == "p":
            (p_row, p_col) = (r, c)
            while r in range(p_row, in_r) and c in range(in_c, p_col + 1):
                if house_map[r + 1][c - 1] not in ("X", "@"):
                    r += 1
                    c -= 1
                    if r >= in_r or c <= in_c:
                        return False
                else:
                    break
            break
        else:
            r -= 1
            c += 1

# Combining all the parts of the diagonal into one
# True basically means that a successor is possible in this location
def diagonal_condition(house_map,r,c):
    if right_bottom_diagonal(house_map, r, c) is False:
        return False
    elif left_top_diagonal(house_map, r, c) is False:
        return False
    elif right_top_diagonal(house_map, r, c) is False:
        return False
    elif left_bottom_diagonal(house_map, r, c) is False:
        return False
    else:
        return True

# This function checks the whole column for possible new insertion points of "p"
def col_check(house_map,r,c):
    p_col_loc_list = []
    [p_col_loc_list.append(i) for i in range(0, len(house_map)) if house_map[i][c] == "p"]
    #print(p_col_loc_list)
    if p_col_loc_list is []:
        return True
    else:
        top_list = [x for x in p_col_loc_list if x < r]
        bottom_list = [x for x in p_col_loc_list if x > r]
        iter_list = []
        #max(top_list),min(bottom_list)] if top_list=[]
        if top_list != []:
            iter_list.append(max(top_list))
        if bottom_list != []:
            iter_list.append(min(bottom_list))
        #print(iter_list)
        state2 = True
        for p_col_loc in iter_list:
            x_col_loc_list = [j for j in range(min(r, p_col_loc) + 1, max(r, p_col_loc)) if house_map[j][c] in ("X", "@")] if p_col_loc is not None else None
            x_col_loc = x_col_loc_list[0] if (x_col_loc_list != [] and x_col_loc_list is not None) else None
            #print(x_col_loc)
            state2 = state2 and (True if (p_col_loc is None) or (p_col_loc is not None and x_col_loc is not None and x_col_loc in range(min(p_col_loc, r),max(p_col_loc, r))) else False)
            #state2.append(True if (p_col_loc is None) or (p_col_loc is not None and x_col_loc is not None and x_col_loc in range(min(p_col_loc, r),max(p_col_loc, r))) else False)
        return state2

# Checks the whole row for possible successors
def row_check(house_map, r, c):
    p_row_loc_list = []
    [p_row_loc_list.append(i) for i in range(0, len(house_map[0])) if house_map[r][i] == "p"]
    # p_row_loc = min(p_row_loc_list, key=lambda x: abs(x - c)) if p_row_loc_list != [] else None
    # print(p_row_loc_list)
    if p_row_loc_list is []:
        return True
    else:
        left_list = [x for x in p_row_loc_list if x < c]
        right_list = [x for x in p_row_loc_list if x > c]
        # print(left_list)
        # print(right_list)
        iter_list = []
        if left_list != []:
            iter_list.append(max(left_list))
        if right_list != []:
            iter_list.append(min(right_list))
        # print(iter_list)
        state1 = True
        for p_row_loc in iter_list:
            x_row_loc_list = [j for j in range(min(c, p_row_loc) + 1, max(c, p_row_loc)) if
                              house_map[r][j] in ("X", "@")] if p_row_loc is not None else None
            x_row_loc = x_row_loc_list[0] if (x_row_loc_list != [] and x_row_loc_list is not None) else None
            state1 = state1 and (True if (p_row_loc is None) or (
                        p_row_loc is not None and x_row_loc is not None and x_row_loc in range(min(p_row_loc, c),
                                                                                               max(p_row_loc,
                                                                                                   c))) else False)
        return state1

# This function combines all the three conditions - row, column and diagonal. This return true only when all three conditions are
# satisfied.
def agent_condition(house_map,r,c):

    #state1 = True if (p_row_loc is None) or (p_row_loc is not None and x_row_loc is not None and x_row_loc in range(min(p_row_loc, c)+1,max(p_row_loc, c))) else False
    #state2 = True if (p_col_loc is None) or (p_col_loc is not None and x_col_loc is not None and x_col_loc in range(min(p_col_loc, r)+1,max(p_col_loc, r))) else False
    state1 = row_check(house_map, r, c)
    state2 = col_check(house_map, r, c)
    state3 = diagonal_condition(house_map,r,c)

    if (state1 and state2 and state3) is True:
        return True
    else:
        return False

# Checking if we reached goal state with k p's
def is_goal(house_map, k):
    return count_pichus(house_map) == k

# Successor function checking if a particular location has an empty space and checking for row,column and diagonal conditions
def successors(house_map):
   return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if (house_map[r][c] == '.' and agent_condition(house_map,r,c)) is True]

# With initial, successor and goal states in place, we solve and iterate all over the house map to look for possible positions of p
def solve(initial_house_map,k):
    fringe = [initial_house_map]
    while len(fringe) > 0:
        for new_house_map in successors(fringe.pop(0)):
            if is_goal(new_house_map,k):
                return(new_house_map,True)
            fringe.append(new_house_map)


if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    #house_map = parse_map(str(sys.argv[0]).split("/arrange_pichus")[0]+"/map1.txt")
    #house_map = parse_map(str(sys.argv[0]).split("/venv")[0] + "/map1.txt")
    # This is k, the number of agents
    # house_map = parse_map(str(sys.argv[0]).split("/venv")[0]+"/map1.txt")
    #k=5
    k = int(sys.argv[2])
    #k = 4
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    if is_goal(house_map,k):
        solution = (house_map, True)
    else:
        solution = solve(house_map,k)
    print ("Here's what we found:")
    if solution is None:
        print("False")
    else:
        print (printable_house_map(solution[0]) if solution[1] else "False")


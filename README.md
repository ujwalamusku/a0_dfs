# a0, Name: Ujwala Musku


**Part 1: Navigation**

**Initial State:** The house map that is divided into n (say) rows and m (say) columns with exactly one agent (p) in a certain position and one destination (@) and a bunch of walls (X) that agent cannot pass.

**Goal State:** Starting from agent’s “p” initial position, the shortest Manhattan distance (with cost of each step to be 1) and the respective path (in terms of movements i.e., up(U), down(D), right(R), left(L)) to destination “@”.

**Cost Function:** The number of steps (U, D, R, L) from agent “p” to destination “@”.

**Successor Function:** Set of all possible movements/positions from agent’s position (initial or later) except the previously visited positions of p.

**Valid States:** All states of house map (nxm matrix) with exactly one agent “p”, one destination “@”, obstacles “X”, and empty spaces “.”.

**Why does the program often fail to find a solution?**
The program fails to find a solution because it is entering indefinite loop when we allow the agent to visit the already visited states to be visited again. 

**Fix:**
Following are the steps taken to fix the code
1.	Create a list to save the once visited positions of the agent, so that before taking a further step later in the problem, we can easily check if we are visiting the already visited position again and filter out such successor positions.
2.	Initially my plan was to push the positions into the fringe one by one but finding the shortest path would be an additional task since I will keep popping the first element in the fringe. Hence, as discussed in the class, I implemented a function that stores the path travelled by agent (in terms of matrix position) as a list and appended that to the fringe instead of appending just an element. Therefore, while checking the next valid successors of the agent, I picked the whole path as an element, sliced it in such a way that it returns the last visited position and looked for valid successors (not previously visited) from that location (after checking if we reached the goal state).
3.	Once we have the shortest path followed by the agent in terms of matrix position, we still need to output the path in terms of movements (U, R, L and D). Therefore, I wrote a function that returns the movements when we input two matrix positions. The function is written in such a way that it only accepts Manhattan distance movements (i.e., one step to the left, right, up and down) and not Euclidean movements (i.e., diagonal).
4.	Since I am appending the path into the fringe rather than one position as an element, the initial fringe is going to be list of a list. It is easy to pop the first element (path) if it’s a list within another list.
5.	After checking through the house map and pushing the paths to the fringe, if there is no path between agent “p” and the destination “@”, the code returns -1. If not, the code returns the path followed and the number of steps.


**Part 2: Hide and Seek**

**Initial State:** The house map with exactly one agent “p” and possible presence of obstacles such as walls (X) or me (@).

**Goal State:** The house map with k number of agents “p” such that they don’t see each other (not in the same row, column and diagonal). If multiple agents are on the same row, column, and diagonal, there needs to be an obstacle (“X” or “@”) in between the agents(“p”).

**Cost Function: **There is no cost in this case because only final state (house map with k agents without seeing each other) in required.

**Successor Function:** Set of house maps (NxM matrix) with exactly 1, 2, ……..(till k) agents while making sure that any two agents can’t see each other (not in the same row, column, and diagonal with no obstacles in between).

**State Space:** All states of house map (nxm matrix) with agents till k and possible presence of obstacles such as “X” or “@”

**Steps followed:**
1.	Created a function that checks the agent’s location “p” in a specific row. In the function, we initially save the nearest agent’s location “p” in both directions (right and left). If there is no agent, we return true. If there is an agent “p”, we check for the obstacle location (“X” or “@”) is in between insertion position and agent location. If yes, we return true, else false. This row function basically returns a Boolean value “True” if it’s a valid agent position for that row.
2.	Created a function that checks the agent’s location “p” in a specific column. Similar to the row function, we look for agent’s location and if found, we look for obstacle location. This function returns a Boolean value as true if it’s a valid agent position for that column.
3.	Created a function that checks the agent’s location “p” diagonally (both right and left diagonals). Since the increments and decrements keep varying for both left and right diagonals, I wrote 4 functions that check the top and bottom parts of each diagonal.
4.	If all the three functions return true, we go ahead and consider the position as the valid successor state.
5.	We find the agent’s location, look for valid successors (row, column, and diagonal check) from the agent’s location, and insert an additional agent in that position. We keep on doing that in each of the empty space and append it to the fringe. After the second agent is added, we do the same process for third agent until we reach k agents. We will keep popping the first element i.e, breadth for search while iterating over the fringe. As soon as we find the house map with k agents placed in positions that doesn’t compromise the conditions (row, column, and diagonal), we break the loop and return the house map. If we don’t find a solution, we return false.

s = 'pqpqs'
num = 2

res = []

l = 0
cur = {}
r = 0
for i in range(len(s)):
    cur[s[i]] = cur.get(s[i], 0) + 1
    if len(cur) == num:
        r = i
        break

res.append(s[l: r + 1])

for right in range(r + 1, len(s)):
    if s[right] in cur:
        cur[s[right]] += 1
        res.append(s[l: right + 1])

        temp = cur.copy()
        ts = res[-1]
        for j in range(len(ts)):
            temp[ts[j]] -= 1
            if temp[ts[j]] != 0:
                if ts[j + 1:] not in res:
                    res.append(ts[j + 1:])
            else:
                break
    else:
        while 1:
            cur[s[l]] -= 1
            if cur[s[l]] == 0:
                del cur[s[l]]
                l += 1
                break
            l += 1
        cur[s[right]] = cur.get(s[right], 0) + 1
        res.append(s[l: right + 1])

        temp = cur.copy()
        ts = res[-1]
        for j in range(len(ts)):
            temp[ts[j]] -= 1
            if temp[ts[j]] != 0:
                if ts[j + 1:] not in res:
                    res.append(ts[j + 1:])
            else:
                break
print(res)

'''

Idea:
    - Perform a DFS using explicit stack to investigate all the paths
    - for each path, once the leaf nodes is reached (the node that lies at matrix[m-1][n-1]), update maxCount
    - Since we are only allowed to traverse to right and down (the matrix bascially becomes a diamond-shaped DAG, or a binary DAG)
    and the time complexity becomes O(P) where P is the number of paths. 
    - cannot afford to use a visited set because more than one paths will go through the same nodes, so we can't miss with that

    P (number of paths) = (m-1) + (n-1)! / (m-1)! * (n-1)!
    time: O(P)

Now of course the DP solution has a time complexity of O(num of nodes) which is far more superior to O(num paths)of the DFS solution.

DP O(num nodes) > DFS O(num of paths)
'''


def pathMaxScore(m):
    startVal = m[0][0]
    startCoor = (0, 0)
    stack = [(startVal, startCoor, [])]  # [] bcuz problem says path should exlude start and end
    dirs = [(1, 0), (0, 1)]  # only right and down are allowed
    maxScore = 0
    while stack:
        node, coor, path = stack.pop()
        x, y = coor

        # check if leaf node (aka the mth, nth cell) is reached
        if x == len(m) - 1 and y == len(m[0]) - 1:
            maxScore = max(maxScore, min(path[:-1]))  # path[:-1] bcuz problem says exclude end
            # count += 1

        for dir in dirs:
            newX, newY = x + dir[0], y + dir[1]
            # within bounds:
            if newX >= 0 and newX <= len(m) - 1 and newY >= 0 and newY <= len(m[0]) - 1:
                stack.append((m[newX][newY], (newX, newY), path + [m[newX][newY]]))

    return maxScore


'''
Version 2 of DFS
Instead of building the entrie path then get min(path)
use a min_sofar variable (less space)
'''


def pathMaxScore_v2(m):
    stack = [((0, 0), m[0][0], float('inf'))]
    max_score = 0
    dirs = [(0, 1), (1, 0)]
    while stack:
        (x, y), node, min_sofar = stack.pop()

        if x == len(m) - 1 and y == len(m[0]) - 1:  # last cell:
            max_score = max(max_score, min_sofar)

        for dir in dirs:
            new_x, new_y = x + dir[0], y + dir[-1]
            if new_x >= 0 and new_x <= len(m) - 1 and new_y >= 0 and new_y <= len(m[0]) - 1:
                if not (new_x == len(m) - 1 and new_y == len(m[0]) - 1):
                    stack.append(((new_x, new_y), m[new_x][new_y], min(min_sofar, m[new_x][new_y])))
                else:
                    stack.append(((new_x, new_y), m[new_x][new_y], min_sofar))

    return max_score


'''
DP solution

# there's only way to build up the path
        # as long as no two paths to choose from we just do min
        # if two paths lead to current cell, then I will have to favor max
'''


def pathMaxScore_DP(m):
    # top most row
    for i in range(2, len(m[0])):  # starts from 2 cuz first cell should be excluded as per writeup
        m[0][i] = min(m[0][i], m[0][i - 1])
    # left most col
    for i in range(2, len(m)):
        m[i][0] = min(m[i][0], m[i - 1][0])
    # rest of grid
    for i in range(1, len(m)):
        for j in range(1, len(m[0])):
            if i == len(m) - 1 and j == len(m[0]) - 1:
                m[i][j] = max(m[i - 1][j], m[i][j - 1])
            else:
                m[i][j] = min(m[i][j], max(m[i - 1][j], m[i][j - 1]))

    return m[len(m) - 1][len(m[0]) - 1]


# m = [[5, 1],[4, 5]] # Output: 4
# m = [[6,2,3], [4,5,6], [7,8,9]] # Output: 4
# m = [[6,2,3], [44,5,6], [7,8,9]] # Output: 7
m = [[1, 2, 3], [4, 5, 1]]  # Output = 4
# m = [[1,9,9],[9,9,9],[9,9,9]] # Output = 9

print(' -- max score path -- O(num of paths)')
print(pathMaxScore(m))

print(' -- max score path V2 -- O(num of paths)')
print(pathMaxScore_v2(m))

print(' -- max score path - DP -- O(num of nodes) --')
print(pathMaxScore_DP(m))

print('----*-----*-----')
print('for a 3x3 grid: ')
print('DP time complexity O(num_nodes = 9) ')
print('DFS time complexity O(num_paths = 40) ')






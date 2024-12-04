
from collections import deque


words = []

dirs = [(1,0), (0, 1), (-1, 0), (0, -1), (1,1), (-1,-1), (1,-1), (-1, 1)]


def dfs(words, i, j, n, m, search, dir):
    if i < 0 or i >= n or j < 0 or j >=m:
        return False
    if words[i][j] != search[0]:
        return False
    
    if words[i][j] == search[0] and len(search) == 1:
        return True
    
    x, y= dir
    return dfs(words, i+x, j+y, n, m, search[1:], dir)
    

    
def search_part1(words):
    n = len(words)
    m = len(words[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            for dir in dirs:
                if dfs(words, i, j,n,m,"XMAS", dir):
                    ans += 1
    return ans

def search_max(words, start, end):
    start_i, start_j = start
    end_i, end_j = end
    
    # check center
    if words[start_i+1][start_j+1] != "A":
        return False
    
    if words[start_i][start_j] == "M" and words[end_i][end_j] == "S":
        if words[start_i][start_j+2] == "M" and words[start_i+2][start_j] == "S":
            return True
        if words[start_i+2][start_j] == "M" and words[start_i][start_j+2] == "S":
            return True
    
    if words[end_i][end_j] == "M" and words[start_i][start_j] == "S":
        if words[end_i-2][end_j] == "M" and words[end_i][end_j-2] == "S":
            return True
        if words[end_i][end_j-2] == "M" and  words[end_i-2][end_j] == "S":
            return True
    
    return False


def search_part2(words):
    n = len(words)
    m = len(words[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            start = (i, j)
            end = (i+2, j+2)
            if i+2 >= n or j+2 >=m :
                continue
            if search_max(words, start, end):
                ans += 1
    return ans

with open("input.txt", "r") as f:
    for line in f:
        words.append([c for c in line.rstrip()])
print(search_part1(words))
print(search_part2(words))

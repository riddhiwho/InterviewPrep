from collections import deque

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","1","0"],
  ["0","0","0","0","0"],
  ["0","0","0","1","1"]
]

visited = [["0"] * len(grid[0]) for _ in range(len(grid))]
# print(visited)

def bfs(row, col, visited, grid):
    visited[row][col]='1'
    queue = deque()
    queue.append([row, col])
    
    while queue:
        node = queue.popleft()
        row = node[0]
        # print("row", row)
        col = node[1]
        # print("col", col)
        n = len(grid)
        m = len(grid[0])

        # traverse the neighbors
        for delrow in range(-1, 2):
            for delcol in range(-1, 2):
                # print(delrow)
                # print(delcol)
                nrow = row+delrow
                ncol = col+delcol
                if 0<=nrow<n and 0<=ncol<m and grid[nrow][ncol]=="1":
                    if visited[nrow][ncol]=="0":
                        visited[nrow][ncol]="1"
                        queue.append([nrow, ncol])
                        print([nrow, ncol])
                

def total_num_islands(grid):
    total_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='1' and visited[i][j]=='0':
                    print("co-ordinates", i, j)
                    total_islands+=1
                    print("total islands", total_islands)
                    bfs(i, j, visited, grid) 
    return total_islands

print(total_num_islands(grid))
                
from collections import deque

T = int(input())

field = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y) :

    queue = deque([])
    queue.append((x,y))
    field[x][y] = 0


    while queue :

        x, y = queue.popleft()
    
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N :

                    continue
            
            if field[nx][ny] == 1:

                field[nx][ny] = 0
                queue.append((nx,ny))




    

for i in range(T) :

    N, M, V = map(int, input().split(" "))

    for j in range(M) :

        field.append([0] * N)

    for k in range(V) :

        x, y = map(int, input().split(" "))
        field[y][x] = 1

    count = 0

    for a in range(M) :

        for b in range(N) :

            if field[a][b] == 1 :

                bfs(a,b)
                count = count + 1
                
    print(count)
    
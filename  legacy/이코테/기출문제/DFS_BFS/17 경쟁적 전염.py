from collections import deque

N, K = map(int, input().split())
graph = []
virus = [] #바이러스 종류 저장
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] != 0: #해당 위치에 바이러스가 존재하는 경우
            virus.append(((graph[i][j], i, j))) #바이러스 종류, 위치x, 위치y
S, X, Y = map(int, input().split()) #초, 위치 x,y

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(s, X, Y):
    q = deque(virus)
    count = 0
    while q:
        if count == s: #시간초 다되면 break
            break
        for _ in range(len(q)):
            prev, x, y = q.popleft() #바이러스 종류 , 위치
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N: #해당 위치로 이동할 수 있는지?
                    if graph[nx][ny] == 0: #바이러스가 방문하지 않았다면?
                        graph[nx][ny] = graph[x][y]
                        q.append((graph[nx][ny], nx, ny))
        count += 1
    return graph[X - 1][Y - 1]


virus.sort() #맨 앞 원소를 기준으로 오름차순 정렬 (바이러스 값을 기준으로 BFS를 수행해서 숫자가 낮은 바이러스부터 우선 탐색)
print(bfs(S, X, Y))

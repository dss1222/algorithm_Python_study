import sys  #여러줄을 입력받아야 하므로 임포트해줌
from collections import deque #컬렉션 모듈의 deque모듈을 사용할 것
#deque는 앞과 뒤에서 데이터를 처리할 수 있는 양방향 자료형이다.
#양방향이기 때문에 스택(stack)처럼 써도 되고 큐(Queue)처럼 써도 된다.
queue = deque()
N = int(sys.stdin.readline())

for _ in range(N):
    i = sys.stdin.readline().split() #변수 i로 split()으로 나눠서 리스트로 값을 입력받는다

    if i[0] == 'push': #push는 queue에 넣는 것이기 때문에queue.append()로 값을 넣어준다
        queue.append(int(i[1]))

    elif i[0] == 'pop': #pop은 queue에서 꺼내는 것이기 때문에 가장 앞에있는 정수를 queue[0]으로 출력하고
        if not queue: #queue.popleft()로 꺼내준다 없는 경우에는 -1을 출력한다
            print(-1)
        else:
            print(queue[0])
            queue.popleft()

    elif i[0] == 'size': #size는 len을 이용해서 queue의 크기를 출력한다
        print(len(queue))

    elif i[0] == 'empty': #empty는 le(queue)로 크기를 재서 비어있으면 1, 아니라면 0을 출력하게 한다.
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif i[0] == 'front': #정수가 들어있지 않는 경우에는 -1을 출력하고 아니라면 queue[0]로 가장 앞에있는 수를 출력한다
        if not queue:
            print(-1)
        else:
            print(queue[0])

    elif i[0] == 'back': #정수가 들어있지 않는 경우에는 -1을 출력하고 아니라면 queue[-1]로 가장 뒤에있는 수를 출력한다
        if not queue:
            print(-1)
        else:
            print(queue[-1])
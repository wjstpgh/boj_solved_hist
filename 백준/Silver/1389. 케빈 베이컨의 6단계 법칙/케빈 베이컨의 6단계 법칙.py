from collections import deque
#너비탐색 시작
def bfs(graph,start):
    num=[0]*n#각 점으로 찾아가는 경로 기록
    visit=[start]#시작점부터 방문여부 표시
    q=deque()
    q.append(start)
    while q:#모든 자식노드 큐에 저장후 모두 탐색
        a=q.popleft()
        #제일 최우선 노드의 간선 모두 탐색
        for i in graph[a]:
            #현 노드의 자식노드가 방문되지 않았다면
            if i not in visit:
                #현 노드의 탐색카운터에 1을 더해 기록
                num[i]=num[a]+1
                #현 노드 탐색여부 기록
                visit.append(i)
                q.append(i)
    #모두 탐색 후 각 카운터합 리턴
    return sum(num)
n,m=map(int,input().split())
#각 그래프의 간선관계도 입력받아 만들기
graph=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(lambda x:int(x)-1,input().split())
    graph[a].append(b)
    graph[b].append(a)
baken=[]
for i in range(n):
    baken.append(bfs(graph,i))
print(baken.index(min(baken))+1)
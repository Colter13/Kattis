from collections import defaultdict

def calc_distance(x_start, y_start, x_end, y_end):
     if x_start == x_end and y_start == y_end:
         return 0
     return (abs(x_end - x_start) + abs(y_end - y_start))**2
def dijkstra(graph, start, end):
    from heapq import heappush, heappop
    dist = {node: float("inf") for node in graph.keys()}
    dist[start] = 0
    pq = [(0, start)]
    processed = set()
    path = {i:[0, i] for i in range(1, len(graph))}
    path[0] = [0]
    while pq:
        cost, node_a = heappop(pq)
        if node_a == end:
            for i in range(len(graph)):
                print(graph[i])
            print(path)
            return cost
        if node_a in processed: continue
        processed.add(node_a)
        
        for node_b, w in graph[node_a]:
            if dist[node_b] > dist[node_a] + w:
                dist[node_b] = dist[node_a] + w
                print(path)
                path[node_b] = path[node_a].copy()
                path[node_b].append(node_b)
                heappush(pq, (dist[node_b], node_b))

    return dist[end] if end in dist else float('inf')

n = int(input())

shade = []

for i in range(n):
    x, y = map(int, input().split())
    shade.append((x, y))
    
start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))

spots = [start] + shade + [end]
graph = defaultdict(list)

for i in range(n + 2):
    for j in range(n + 2):
        graph[i].append((j, calc_distance(spots[i][0], spots[i][1], spots[j][0], spots[j][1])))

for i in range(len(graph)):
    print(graph[i])

print(dijkstra(graph, 0, n + 1))
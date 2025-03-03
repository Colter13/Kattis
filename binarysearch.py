n, m = map(int, input().split())

values = list(map(int, input().split()))
value = {i+1:values[i] for i in range(n)}

edges = {}


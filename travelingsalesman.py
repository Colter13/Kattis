import itertools

def held_karp(dists): # n x n Distance matrix from node A to node B
    n = len (dists)
    C = {} # C|(subset_mask, k)] = (cost, previous_k)
    for k in range (1, n):
        C[(1 << k, k)] = (dists[0][k], 0)
    # Dynamic programming: choose best subsets based on smaller subsets
    for subset_size in range (2, n):
        for subset in itertools.combinations(range (1, n), subset_size):
            # Encode this subset as bitmask
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            # Find the lowest cost to get to this subset
            for k in subset:
                prev = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                res.append((C[(prev, m)][0] + dists[m][k], m))
            C[(bits, k)] = min(res)
    bits = (2**n - 1) - 1
    res = []
    for k in range (1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt, parent = min(res)
    # Backtrack to find shortest path
    path = []
    for i in range(n - 1): 
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits
    path.append(0)
    return opt, list(reversed(path))

while True:
    n = int(input())
    if n == 0:
        exit()
    
    
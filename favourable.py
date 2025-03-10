for _ in range(int(input())):
    s = int(input())

    d = {}

    favourable = []
    for __ in range(s):
        i, *x = input().split()
        i = int(i)
        x = list(map(int, x)) if x[0] not in ['favourably', 'catastrophically'] else x

        if len(x) == 1:
            d[i] = 1 if x[0] == 'favourably' else 0
        else:
            d[i] = x

    def parse(i):
        if isinstance(d[i], list):
            total = parse(d[i][0]) + parse(d[i][1]) + parse(d[i][2])
            d[i] = total
        return d[i]


    print(parse(1))
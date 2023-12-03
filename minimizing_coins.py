n, inp = map(int, input().split())
coins = list(map(int, input().split()))

def minimizing_coins(n: int, coins: list) -> int:
    d = {n: 0}
    f = [n]
    while len(f) > 0:
        k = f.pop()
        v = d.get(k)
        for i in coins:
            e = d.get(k - i, -1)
            if (v + 1 < e or e == -1) and k - i >= 0:
                d[k - i] = v + 1
                f.append(k - i)
    return d.get(0, -1)

print(minimizing_coins(inp, coins))
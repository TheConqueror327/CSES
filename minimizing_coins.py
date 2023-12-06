n, inp = map(int, input().split())
coins = list(map(int, input().split()))

def minimizing_coins(n: int, coins: list) -> int:
    d = [-1] * (n + 1)
    d[n] = 0
    f = [n]
    while len(f) > 0:
        k = f.pop()
        v = d[k]
        for i in coins:
            if k - i >= 0:
                e = d[k - i]
                if (v + 1 < e or e == -1):
                    d[k - i] = v + 1
                    f.append(k - i)
    return d[0]

print(minimizing_coins(inp, coins))
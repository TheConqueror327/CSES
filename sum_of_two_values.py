n, xx = map(int, input().split())
lis = list(map(int, input().split()))

def sum_of_two_values(li: list, x: int) -> int:
    for i, v in enumerate(li):
        for o, w in enumerate(li[i+1:]):
            if v + w == x:
                return f'{i + 1} {o + i + 2}'
    return 'IMPOSSIBLE'

print(sum_of_two_values(lis, xx))

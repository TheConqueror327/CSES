n, xx = map(int, input().split())
lis = list(map(int, input().split()))

def sum_of_two_values(li: list, x: int) -> int:
    for i, v in enumerate(li):
        for o, w in enumerate(li[i:]):
            if v + w == x:
                return f'{o + 1} {i + 1}'
    return 'IMPOSSIBLE'

print(sum_of_two_values(lis, xx))
def intersects(p1: list, p2: list, p3: list) -> str:
    if p3[0] / p3[1] > p1[0] / p1[1]:
        return 'LEFT'
    elif p3[0] / p3[1] < p1[0] / p1[1]:
        return 'RIGHT'
    else:
        return 'TOUCH'
    
#print(intersects([-1, -1], [1, 1], [2, 1]))
tests = []
for i in range(3):
    tests.append(list[map(int, int(input().split()))])

print(tests.pop(0))
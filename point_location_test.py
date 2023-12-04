def intersection(p1: list, p2: list, p3: list) -> str:
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = p1[1] - m * p1[0]
    if p3[1] > m * p3[0] + b:
        return 'LEFT'
    if p3[1] < m * p3[0] + b:
        return 'RIGHT'
    return 'TOUCH'

def faster_intersection(p1: list, p2: list, p3: list) -> str:
    if (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) > 0:
        return 'LEFT'
    elif (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) < 0:
        return 'RIGHT'
    return 'TOUCH'

t = int(input())

for i in range(t):
    current_test = list(map(int, input().split()))
    print(faster_intersection(current_test[:2], current_test[2:4], current_test[4:]))
def removing_digits(n: int):
    steps = 0
    while n != 0:
        n -= max([int(i) for i in str(n)])
        steps += 1
    return steps

print(removing_digits(int(input())))
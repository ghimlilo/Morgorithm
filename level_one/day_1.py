n, m = map(int, input().split())
i = 0
while i < m:
    j = 0
    while j < n:
        print('*', end='')
        j = j+1
    print()
    i = i+1
def solution(x, n):
    a = []
    num = x
    while len(a) < n:
        a.append(num)
        num += x 
    return print(a)

x, n = map(int, input().split(','))
solution(x, n)



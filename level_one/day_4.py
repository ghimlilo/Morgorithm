# 부끄러운 내 풀이
# def solution(phone_number):
#     list = []
#     for i in phone_number[0:-4]:
#         i = i.replace(i, '*')
#         list.append(i)
#     result = list+[phone_number[-4:]]
#     print(''.join(result))

# result = solution('011100000001234')

#은찬님 풀이

# def solution(phone_number):
#     a = phone_number[:-4]
#     b = '*' * len(a)
#     print(phone_number)
#     return print(phone_number.replace(a, b))
# result = solution('011100000043434')

#기가막힌 답

def solution(phone_number):
    return print('*'*(len(phone_number)-4) + phone_number[-4:])

result = solution('011100000001234')

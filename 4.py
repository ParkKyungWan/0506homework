answer =0
for i in range(999,0,-1):
    for j in range(999,0,-1):
        곱한값 = i*j
        문자_곱한값 = str(곱한값)
        if 문자_곱한값 == 문자_곱한값[::-1] and 곱한값>answer:
            answer = 곱한값
print(answer)
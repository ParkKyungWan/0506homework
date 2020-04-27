answer =0
for i in range(999,0,-1):
    for j in range(999,0,-1):
        ㅋ = i*j
        ㄱ = str(ㅋ)
        if ㄱ == ㄱ[::-1] and ㅋ>answer:
            answer = ㅋ
print(answer)
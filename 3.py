N = int(input());
answer =0;
i = 2
while i<N//2+1:
    ㄱㅇㄱ =1
    while N%i ==0:
        ㄱㅇㄱ *= i
        N//=i
    if ㄱㅇㄱ>answer:
        answer = ㄱㅇㄱ
    i+=1
print(answer if answer>N else N)
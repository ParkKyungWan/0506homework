N = int(input());
answer = 0;
i = 2
while i<N // 2+1:
    j = 1
    while N % i == 0:
        j *= i
        N //= i
    if j > answer:
        answer = j
    i += 1
print(answer if answer > N else N)
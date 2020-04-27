answer,i,j = 2,1,2
MAX = 4000000

while j<=MAX:
    for n in range(3):
        i=i+j
        i,j=j,i
    answer+= j if (j<=MAX) else 0;
print(answer)


#2 이후로 홀수,홀수,짝수의 형태가 반복됩니다.
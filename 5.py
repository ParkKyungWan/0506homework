answer = 1
발자취 = []
for i in range(1,int(input())+1):
    n= i
    for j in 발자취:
        if n%j==0:
            n//=j
    answer*=n
    발자취.append(n)
print(answer)

#중복되는 약수를 제거하여 곱합니다
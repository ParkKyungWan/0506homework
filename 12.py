num = 28
tonext = 8
while num<=500:
    num+=tonext
    tonext+=1

while True:
    tmpnum = num
    약수 = 1
    for i in range(2,num//2+1):
        제곱수 = 0
        while tmpnum%i==0:
            제곱수 +=1
            tmpnum//=i
        약수*=(제곱수+1)
        if i>=tmpnum:
            break;
    if 약수 >=500:
        print(num)
        break;
    num+=tonext
    tonext+=1

#약수의 개수 = 소인수 분해 했을때 (제곱횟수+1) 들의 곱
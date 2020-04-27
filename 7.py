import sys
count = 6
i = 13
gap = 0
while True:
    i+=2
    check = True
    for j in range(2,i//2+1):
        if i%j==0:
            check = False
            break
    if check:
        count+=1
        if count==10001:
            print(i)
            sys.exit()

#너무 느린 코드입니다 ..ㅠ

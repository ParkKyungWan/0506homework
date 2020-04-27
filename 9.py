import sys
c = 333 # 제일 큰 수가 333보다 커야 됌
while True:
    for a in range(1,c):
        for b in range(c-a+1,c): # 두변의 길이의 합 > 다른 한변의 길이
            if a*a+b*b==c*c and a+b+c == 1000:
                print(a,b,c," | ",a*b*c)
                sys.exit();
    c+=1

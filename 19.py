month = [31,28,31,30,31,30,31,31,30,31,30,31]
day = 2 # 1901/01/01은 화요일
answer =0
for now in range(1901,2001):
    if (now%4==0 and now%100!=0) or (now%400==0):
        month[1]= 29
    for m in month:
        if day%7==0:
            answer+=1
        day+=m
    if month[1]==29:
        month[1]=28

print(answer)
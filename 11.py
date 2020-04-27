s = [[int(i) if int(i)>80 else 11 for i in input().split(" ") ] for i in range(20)]

for i in range(20):
    print(s[i])

# 80 밑으로 다 지우면 보입니다..
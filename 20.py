answer= 1
for i in range(100,0,-1):
    answer*=i
print(sum([int(i) for i in str(answer)]))
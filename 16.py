i = 1
for j in range(1000):
    i*=2
print(sum(list(map(int,str(i)))))
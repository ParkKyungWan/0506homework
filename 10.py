#에라토스테네스의 체
def go(n):
  후보=[True]*(n+1)
  for i in range(2, int(n//2)+1):
    if 후보[i] == True:
      for j in range(i+i,n+1,i):
        후보[j]=False
  return sum([i for i in range(2,n) if 후보[i]==True])

print(go(int(input())))
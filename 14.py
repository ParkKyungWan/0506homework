longest_try = 0
longest_num = 0
for i in range(1000000,1,-1):
    now = i
    now_tries = 0
    while now!=1:
        now = now//2 if now%2==0 else 3*now+1
        now_tries +=1
    if now_tries>longest_try:
        longest_num = i
        longest_try = now_tries
print(longest_num)

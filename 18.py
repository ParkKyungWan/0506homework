nums = [list(map(int,input().split(" "))) for i in range(15)]

biggest = 0
def search(floor,index,now):
    if floor< 14:
        result = search(floor+1,index,now+nums[floor][index])
        result2 =  search(floor+1,index+1,now+nums[floor][index])
        if result>result2:
            return result
        else:
            return result2
    else:
        _now = now
        _now += nums[floor][index]
        return _now

print(search(0,0,0))

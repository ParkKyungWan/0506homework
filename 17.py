
# one two three four five six seven eight nine
일= [0,3,3,5,4,4,3,5,5,4]

# ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen
십= [3,6,6,8,8,7,7,9,8,8]

# twenty thirty forty fifty sixty seventy eighty ninety
몇십 = [6,6,5,5,5,7,6,6]

#hundred
백 = 7

answer = sum(일)                        #1~9
answer+= sum(십)                        #10~19
answer += sum(몇십)*10 + sum(일)*8      #20~99
answer += sum(일)*100  +  answer*9  +  백*9  +  ((백+3)*891)
answer += len("onethousand")


print(answer)

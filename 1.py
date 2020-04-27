N = int(input())-1
three,five,exception  = N//3, N//5, N//(3*5)
answer = (three*(three+1)//2)*3 + (five*(five+1)//2)*5
answer -=(exception*(exception+1)//2)*15
print(answer);


#a의 배수 = [a*1,a*2,a*3,,,] 합 = (1+2+3+,,,,)*a
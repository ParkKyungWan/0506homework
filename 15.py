def factorial(num):
    if num ==1:
        return 1
    else:
        return num * factorial(num-1)
사십 = factorial(40)
이십 = factorial(20)
print(사십//(이십*이십))

#n*m 격자에서 (n+m)!/n!m! 개
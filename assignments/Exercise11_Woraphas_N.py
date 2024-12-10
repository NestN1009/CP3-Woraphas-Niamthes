myInput = int(input())
x = 1
for i in range(myInput):
    print((" "*(myInput-x))+"*"*((2*i)+1)+(" "*(myInput-x)))
    x+=1

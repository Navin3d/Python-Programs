n=eval(input("enter a number"))
count=1
num=2
while count<=n:
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)
        count=count+1
    num=num+1

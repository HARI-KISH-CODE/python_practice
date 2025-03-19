num=int(input("enter num: "))
for i in range(2,num):
    if num%i==0:
        print("not prime num ")
        break
else:
    print("prime num")
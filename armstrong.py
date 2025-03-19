num=input("enter a num: ")
length=len(num)
sum=0
for i in num:
    sum+=int(i)**length
if sum==int(num):
    print("strong num")
else:
    print("not strong num")
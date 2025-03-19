def fibi(num):
    fib_series=[0,1]
    for i in range(2,num):
        fib_series.append(fib_series[-1]+fib_series[-2])
    return fib_series

list=fibi(10)
print(list)

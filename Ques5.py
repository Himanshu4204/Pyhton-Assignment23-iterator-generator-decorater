#5. Create a generator to produce first n terms of Fibonacci series?
def fibonacci(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
for x in fibonacci(int(input("Enter a Number :"))):
    print(x)
    
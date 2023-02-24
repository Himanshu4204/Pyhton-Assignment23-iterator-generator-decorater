#7. Create an endless iterator using generator method to produce terms of Fibonacci series?
def fibonacci(n):
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for x in fibonacci(int(input("Enter a Number :"))):
    print(x)

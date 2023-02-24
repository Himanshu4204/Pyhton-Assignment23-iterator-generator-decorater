#4. Create a generator to produce squares of first N natural numbers?
def squares(n):
    for i in range(1,n+1):
        yield i**2
for x in squares(int(input("Enter a Number :"))):
    print(x)


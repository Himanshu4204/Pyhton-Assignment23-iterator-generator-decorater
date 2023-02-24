#2. Create a generator to produce first n odd natural numbers?
def odd(n):
    for i in range(1,2*n,2):
        yield i
for x in odd(int(input("Enter a Number :"))):
    print(x)


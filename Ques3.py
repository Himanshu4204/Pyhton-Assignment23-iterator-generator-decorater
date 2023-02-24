#3. Create a generator to produce first n even natural numbers?
def even(n):
    for i in range(2,2*n+2,2):
        yield i
for x in even(int(input("Enter a Number :"))):
    print(x,end=' ')


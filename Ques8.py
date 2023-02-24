#8. Create an endless iterator using generator method to produce Prime numbers?
def prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def prime_Generator(n):
    num=2
    while True:
        if prime(num):
            yield num
            n-=1
        num+=1
    return
it=prime_Generator(int(input("Enter how many prime numbers you want:")))
for x in it:
    print(x)
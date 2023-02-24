#10. Define a function which calculates HCF of two numbers. Define and apply a
#    decorator to check whether two given numbers are co-prime or not.
def decor_coprime(func):
    def is_coprime(num1,num2):
        for i in range(1,min(num1,num2)+1):
            if num1%i==0 and num2%i==0:
                x=i
        if x==1:
            print("Yes it is Co-Prime Number")
        else:
            print("Not co-prime Numbers! ")
        func(num1,num2)
    return is_coprime

@decor_coprime
def HCF(num1,num2):
    for i in range(1,min(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            x=i
    print("Hcf of two numbers is :",x)
num1=int(input("Enter First Number :"))
num2=int(input("Enter Second Number :"))
HCF(num1,num2)

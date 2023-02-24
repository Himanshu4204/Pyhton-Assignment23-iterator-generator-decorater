#9. Define a function which takes lengths of three sides of a triangle as arguments and display the perimeter or triangle. 
#   Define and apply a decorator which checks for the validity of the triangle on the basis of lengths of the side. 
#   This makes the perimeter to be displayed when the triangle can exist with the given lengths of the sides. ?
def check_Valid(func):
    def is_valid(l,b,h):
        if l+b<=h or b+h<=l or h+l<=b:
            print("Not a Valid Triangle")
        else:
            func(l,b,h)
    return is_valid

@check_Valid
def check_Perimeter(l,b,h):
    sum=l+b+h
    print("Perimeter of the tiangle is :",sum)

l=int(input("Enter length of the Triangle :"))
b=int(input("Enter Breadth of the Triangle :"))
h=int(input("Enter Height of the Triangle :"))

check_Perimeter(l,b,h)


#1. Use iter and next method to access all the elements of a given set using while loop?
s1={10,20,30,40,50,60}
it=iter(s1)
while True:
    try:
        print(next(it))
    except:
        break
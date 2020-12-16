c0 = int(input("enter a number: "))
x=0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0/2
        print(int(c0))
        x=x+1
    else:
        c0 = 3*c0+1
        print(int(c0))
        x=x+1
print("this ended in ",x," steps")

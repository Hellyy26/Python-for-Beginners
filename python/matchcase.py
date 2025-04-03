# in a python there is simiilert to switch statement match
# break statement not use in this
x=int(input("enter the value of x"))
match x:
    case 0:
        print("x is zero")
    case 2:
        print("x is 2")
    case 4:
        print("x is 4")  
    case _:
        print(x)      
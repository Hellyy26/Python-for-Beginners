# the finnaly part always exucutes 
# it is also part of error handling

try:
    num=int(input("enter num"))
except:
    print("sum error occurs")
finally:
    print("its always exucte")


#one of main use of finnaly is in fucntion which return as value
 
try:
    num=int(input("enter num"))
except:
    print("sum error occurs")

print("its always exucte") 
# in normal flow this print runs but in function this not runs
# so in funxtion finnaly runs always after return the value

def fun1():
    try:
        a=[10,20,30]
        num=int(input("enter num"))
        
        print(a[num])
        return 1
    
    except IndexError:
        print("inavlid index")
        return 0
    finally:
        print("its always exucte")

ans=fun1()
print(ans)

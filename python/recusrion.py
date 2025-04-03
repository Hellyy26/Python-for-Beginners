# when a function call it self than it is called recusion function

# factorial(5)=5*4*3*2*1
# factorail(4)=4*3*2*1
# factorail(3)=3*2*1

# factorail(n)=n*factorial(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))    

# n=5
# 5*factorial(4)
# it goes again to find value of fact 4 now value of n=4 so find fact 3
# 5* 4* factorail(3)
# it goes again to find value of fact 3 now value of n=3 so find fact 3
# 5* 4* *3 factorail(2)
# it goes again to find value of fact 2 now value of n=2 so find fact 12
# 5* 4* 3* 2* factprial(1)




# find the fibonnachi seriss
# f(0)=0
# f(1)=1
# f(2)=f(0)+f(1)
# f(n)=f(n-1)+f(n-2)


def fibonnachi(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonnachi(n-1)+fibonnachi(n-2)
    

n=10
print(fibonnachi(n))    


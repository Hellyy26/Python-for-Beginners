# docstrings are string literial taht apper right after the defiantion of function
# method,class,module ex:''' '''
# if we print this we can it not ignore like comments
# docstring is just after function defination we define


def square(n):
    ''' this print the perfecr square of 
        n*n
    '''
    print(n**2)
square(5)    

print(square.__doc__)




# MOSTIMP
# this is not docstring
# def square(n):
#     x=10
#     print(x)
#     ''' this print the perfecr square of 
#         n*n
#     '''
#     print(n**2)
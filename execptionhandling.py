# python has many buit in exeptions that are raised when your program encourage an eroor

# 1)try-catch
# try=>try blocks run when there is no KeyError
# catch=>when the try block raises error than catch 

# if there is chance in your program that error occur than cheak this code in
# try block

# a=input("enter a num")
# print(f"multipication of a is {a}")

# try:
#     for i in range(1,11):
#         print(f"{int(a)}*{i}={int(a)*i}")
# except Exception as e:
#     print(e) 
#     # e will print the eroor and below line sucessfulyy execute
# print("imp line")
# print("end of program ")



a=input("enter a num")
print(f"multipication of a is {a}")

try:
    for i in range(1,11):
        print(f"{int(a)}*{i}={int(a)*i}")
except:
    print("invalid input")
    # directly print error using print
    
print("imp line")
print("end of program ") 


# value error
# if the num is int than go to else part
try:
    num=int(input("enter number of int"))
except ValueError:
    print("the value of num is not int")
else:
    print("done thank you")    


# index error    
try:
    num=int(input("enter the index"))
    a=[10,20]
except ValueError:
    print("the num is not int")
except IndexError:
    print("value out of index")
else:
    print(f"the num is find ")    
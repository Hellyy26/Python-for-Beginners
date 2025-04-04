# python has many buit in exeptions that are raised when your program encourage an eroor

# 1)try-catch
# try=>try blocks run when there is no KeyError
# catch=>when the try block raises error than catch 

# if there is chance in your program that error occur than cheak this code in
# try block

a=input("enter a num")
print(f"multipication of a is {a}")

try:
    for i in range(1,11):
        print(f"{int(a)}*{i}={int(a)*i}")
except Exception as e:
print("imp line")
print("end of program ")    
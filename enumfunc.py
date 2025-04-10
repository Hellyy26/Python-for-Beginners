# teh enum function is built in function in python
# the enum function allows you to loop over a sequence and get a index

fruits=["apple","banana","orange"]
for index,fruits in enumerate(fruits):
    print(index,fruits)


marks=[1,4,5,6,7,90,3,56]
for index,marks in enumerate(marks):
    print(index,marks)
    if(index==5):
        print("good helly")    
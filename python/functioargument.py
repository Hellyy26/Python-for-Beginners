# def avg(a,b):
#     print("the avg is",(a+b)/2)

# avg(10,2)    


# there aree 4 types of arguments
# 1.defualt arguemnt
# 2.keyword argument
# 3.varoable length argument
# 4.parameter argument





# 1.defult argumet
# def avg(a=10,b=20):
#     print("the avg is",(a+b)/2)
# avg()    

# if we pass argument duruting function call then it ignore default arguments
# avg(10,2)   





# 2.keyword argument
# we can provide argument as key and value and also change the order
# def name(fname,mname,lname):
#     print("hello",fname,mname,lname)

# name(lname="vyas",mname="vikas",fname="helly")




# 3.required argumet
# it is neccesary to pass argument else give error
# in below program it is neccesary to give value of a and b
# def avg(a,b,c=3):
#     print("the avg is",(a+b+c)/3)
#     # print("the avg is",(a+b)/2)  it onlt take value of a and b (2+5)/2=3.5
# avg(2,5)    
# avg(10) ////TypeError: avg() missing 1 required positional argument: 'b'




# 4.varibale lengtrhbargument
# 1.arbatary
# 2.keyword arbatary


def avg(*num):
    sum=0
    for i in num:
        sum=sum+i
    print("the sum and avg",sum / len(num))

avg(10,20,30,10)        
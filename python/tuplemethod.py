# tuples are immutable if you want to change tuple first you have to convert
# tuple to string 

tup=("india","maldivas","paris","engalnd","austrial")
# print(tup)

# tup.append("london")  'tuple' object has no attribute 'append'
# temp=list(tup)
# temp.append("london")
# temp[1]="ruusia"
# print(temp)

# now we have to convert list to tuple
# tup1=tuple(temp)
# print(tup1)


# t1=(1,2,4,5)
# t2=(9,3,10)
# t3=t1+t2
# print(t3)


# 1=>count()
# t1=(1,2,3,4,3,5,6,3)
# res=t1.count(3)
# print(res)


# 2=>index-give first occurance of given element
# t1=(1,2,3,4,3,5,6,3)
# res=t1.index(3)
# print(res)


# index(element,stratposition,endpostion)
# t1=(1,2,3,4,3,5,6,3)
# res=t1.index(3,3,7)
# print(res)



# len=>prints length of tuple
# t1=(1,2,3,4,3,5,6,3)
# print(len(t1))
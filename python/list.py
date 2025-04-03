# list are ordered collection of data items
# list store multiple item in single variable
# list item are changeable means we can change the item after creation

# list1=[10,20,30]
# print(list1)
# print(type(list1))
# print(list1[0])
# print(list1[1])

# list1=[10,20,30,"hrllu",True,4.6]
# print(list1)
# negetive index -1 means last postion
# print(list1[len(list1)-3])
# print(list1[5-3])
# print(list1[-1])


# list1=[10,20,30,"hrllu",True,4.6]
# if 3 in list1:
#     print("yes")
# else:
#     print("no")

# if "hr" in "hrllu":
#     print("yes")
# else:
#     print("no")



# list1=[10,20,30,"hrllu",True,4.6]
# jump measna is skips 
# # print(list1[1:4:2])

# list1=[1,3,4,5,13,3,5,6,10]
# # print(list1[::2])  
# # # 0:9:2
# # print(list1[0:9:2])

# print(list1[-8:-1:2])
# # list1[9-8:9-1:2]
# # 1:8:2
# print(list1[1:8:2])


# list comaprsion
# lst=[i for i in range(5)]
# print(lst)

lst=[i for i in range(10) if i%2==0]
print(lst)
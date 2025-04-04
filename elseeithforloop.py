# we can use else keyword with for loop and while loop 

# for i in []:
#     print(i)
# else:
#     print("sorry no i")


# # program-2  
# for j in range(5):
#     print(j)
# else:
#     print("this else exicute after 0,1,2,3,4")


for i in range(6):
    print(i)
    if(i==4):
        break

else:
    print("else block")

    # it does not print else block bcoz break indicates that the last 
    # intection is done and out of loop 
 
# j=0
# while j<7:
#     print(j)
#     j=j+1
#     if (j==5):
#         break

# else:
    # print("else with while loop")     -----not execute


 
# j=0
# while j<7:
#     print(j)
#     j=j+1
# else:
#     print("else with while loop")    -------execute


# mostimp:::::when you use break with foor and while and same 
# time you use else than else not execute    
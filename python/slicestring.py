names="helly,alka"
print(len(names))

# slice-method slice method not count last word
print(names[0:5])
print(names[0:7])

# without specify start index it by defualt take 0 index
print(names[:5])

# witout specify anything it take length
print(names[:])

# if we specify index -3 python take it
# len(fruit)-3
# len of variable fruit is 5-3=2 so it print ma
fruit="mango"
print(fruit[0:-3])


# if [-3:-1]
# it is like (len(fruit -3)) means (5-3) and (5-1)
# 2:4 menas it print "ng"
print(fruit[-3:-1])

# quick-quize
# nm="harry" print(nm[-4:-2])
# menas (len(nm-4)) means 5-4=1 and 5-2=3 
# 1:3 menas print "ar"
nm="harry"
print(nm[-4:-2])

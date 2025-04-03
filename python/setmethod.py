# set is collrction of well defined object

# 1)union=>union gives value by combine both set
# s1={1,2,3,4}
# s2={4,5,6}
# print(s1.union(s2))

# update method upadte the real value 

# 2)interction=>retun common from both
# s1={1,2,3,4}
# s2={4,5,6}
# print(s1.intersection(s2))


# 3)symentic diffrence=>menas that value which is not common
s1={1,2,5,3,4}
s2={4,5,6}
print(s1.symmetric_difference(s2))


# superset()=>menas set two value present in set 1
# s1={1,2,3,4,5,6}
# s2={4,5,6}
# print(s1.issuperset(s2))


# add=>adss something
s1={"tokyo","berlin","madrid"}
s1.add("hesinki")
print(s1)

# remove=>removes specific ex:s1.remove("tokyo")
# pop=>remove last element
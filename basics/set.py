#SETS
#There is other type of datatypes like sets
#One set in python is considered as a matemathical set

'''
	There is two type of sets mutable an unmutable sets
		example of one mutable set
			mutable_set = set("88948")

		example of one unmutable set
			unmutable_set = frozenset("88948")

	In one set the data can't be repeated

	The operators like and, or are used with the set defined by constructor mode,
	and the other way operators like &, |

	THE SETS DOESN'T SUPPORT INDEXING, BUT ARE ITERABLES
'''

#The way to declare one set is the following as constructor mode and with {}
myset1 = {8,9,7,4,8}
print(myset1)

myset2 = {5,8,7,9}
print(myset2)

#operations with sets
#intersection
result = myset1 & myset2

print("the result of [myset1 & myset2] is {0}".format(result))

#conjunction
result = myset1 | myset2

print("the result of [myset1 | myset2] is {0}".format(result))
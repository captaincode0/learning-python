'''
	DICTIONARIES

	The dictionary are one special datastructure, in other languages knowed as hashes,
	but one dictionary is one set of types, this structure is mutable, iterable and accesible
	the difference with lists, is that one list has numerical index, and dictionary has numerical
	and string indexes
'''

connection_properties = {"username": "root", "password": "1234"}
print(connection_properties)

#accesing into one element
print(connection_properties["username"])

'''
	Functions to iterate the elements
		values: get all values of the dictionary
		items: get the combination of key,value of one dictionary
		keys: get the keys of one dictionary
'''

#get the values
for data in connection_properties.values():
	print(data)

#get the value and index
for key,value in connection_properties.items():
	print("key [{0}], value [{1}]".format(key, value))

#get the keys of dictionary
for key in connection_properties.keys():
	print("key "+key)

'''
	How to iterate in one redux way all the elements in one dictionary
'''

#create one set mapping other set
target = (1,2,3,4)
factorized_set = {k: k+1 for k in target}
print(factorized_set)

gamma = {"x1": 3000, "x2": 6000, "x3": 78.66}
r_index = 1.6888888
factorized_dic = {key: value+r_index for key,value in gamma.items()}
print(factorized_dic)

'''
	Sort dictionaries
		The dictionaries hasn't one function sorted to order it, but the keys of one dictionary are ordered
'''
print(sorted(connection_properties, reverse=True))
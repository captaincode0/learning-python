#TUPLES
#this is one inmutable and iterable datatype
#THE TUPLES SUPPORT INDEX AND ARE ITERABLES

mytuple = (0,1,2,3,4,5,6)
print(mytuple)

#get the value of one tuple
print(mytuple[0])

try:
	#change the value of one tuple
	mytuple[0] = 2
except TypeError as err:
	print(err)

#the tuples are iterable
for data in mytuple:
	print(data)

#the tuples can be operated
#duplicate the tuple
mytuple1 = mytuple*2
print("The result of mytuple*2 is {0}".format(mytuple1))

'''
	Methods to use the tuples
		count: returns the number of recurrences in one tuple
		index: get the index by one value
'''
print(mytuple.count(2)) #1
print(mytuple.index(6)) #2
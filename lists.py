#LISTS
#The list are one set of mutable objets similar to one array in other programming languages
#The list are mutable and iterables

mylist = [1,2,3,4]

for element in mylist:
	print(element)

#trying to mute one list
mylist[0] = 1000

print(mylist)

#you can check if one element is in one list
print(1000 in mylist)

#the tuples are the mutable equivalence of one list
#you can transform one list into one tuple defining creating one object of type tuple 
#with one list as argument

mytuple = tuple(mylist)
print(mytuple)
print(type(mytuple))

'''
	Implementation methods of one list
		append: adds to the end of one list the element.
		insert(index, element): insert one element in one defined index.
		len: get the longitude of one list.
		del(list[index]): deletes one element in the list given the element
		pop(index): deletes and return the last element in the list.
		remove: deletes by value one element in the list, if its repeated then delete the first occurrence.
'''

#append one value into the list
mylist.append(8);
print(mylist)

#insert one value in the list
mylist.insert(3, 5)
print(mylist)

#get the longitude of one list
print(len(mylist))

#deletes one element in the index zero
del(mylist[0])
print(mylist)

#pop one element at the end of the list like a stack
deleted_node = mylist.pop()
print(deleted_node)

#deletes the number eight
was_removed = mylist.remove(2)

#SORT THE LIST
#exists two methods to sort one list sorted and sort that returns one list changed
#in the method sorted you can use the parameter reverse to get one list in reverse order
sorted_list = sorted(mylist)
print(sorted_list)

reverse_sorted_list = sorted(mylist, reverse=True)
print(reverse_sorted_list)

print("original list: {0}".format(mylist))

#How to order one string list
string_list = ["Df", "Aa", "Ab", "Cd"]
print(string_list)

sorted_string_list = sorted(string_list, key=str.lower)
print(sorted_string_list)

#implementing sort function
print(string_list.sort())
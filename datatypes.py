#In python exists different kind of datatypes
#There is objects and natives data types

x = 2;
y = x;

'''
	In the past example x has the value of 2
		and pass the value to y
			thus x and y has references
				the references are localizable in the memory

	x -> 2
	y -> x
'''

#but what happens if you change the y 
y = "this"

#x is preserved 

print(x)
print(y)

#but when you have a list for example, and you try to change one component of the datastructure

list1 = [1,2]
list2 = list1

list1[0] = 5

print(list1[0]) #5
print(list2[0]) #5

'''
	In the last case prints five and five in the two list because one component
	of the list is changed
'''

#NUMBERS
#There is different type of numbers in python, the real numbers, complex numbers, integers
#Each kind of numbers has it set of operations
'''
						NUMBERS
	INTEGER 			 REAL 			COMPLEX
	BOOLEAN (0,1) 
	[True, False] 
'''

#INTEGER NUMBERS
int_num1 = 89
int_num2 = -89

print(89)
print(-89)

#REAL NUMBERS
#The real numbers contain a part called mantisa

real_number = 125.23546
print(real_number)

#the real numbers contain exponential notation
real_number = 1.5e-7
print(real_number)

#COMPLEX NUMBERS
#The complex numbers are composed by an imaginary and real part Z = a+bj where j = sqrt(-1)

complex_number = 8+3j
print(complex_number)

#NUMERIC SYSTEMS
#binary
binary_number = 0b01100001 #97
print(binary_number)

#octal
octal_number = 0o71 #9
print(octal_number)

#hexadecimal
hex_number = 0x61 #97
print(hex_number)

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

#STRINGS
#In python all the strings has an Unicode representation
#There is two type of strings mutable and unmutable (that can't change its value)
#The unmutable string is defined as byte type
#The mutable string is defined as bytearray type

string = "This is one simple string"
print(string)

#byte string
string = b"This is one unmutable string"
print(string)

#try to chage the string
try:
	string[0] = "a"
	print(string)
except TypeError as e:
	print(e)

#but if you change all the string, it is acceptable
string = "Hello"
print(string)

#as in C one string is one char array you can iterate it
#iterate hello
for char in string:
	print(char)

#the byte array is the mutable version of byte string
string = bytearray("¿Qué hace en España?", "latin1")
print(string)

#The strings implements two methods to handle the byte strings
#decode: transforms one byte string to a normal string
#encode: transform one normal string to one byte string

mystring = b"This is one binary string"
print(mystring)
print(type(mystring)) #The function type get the datatype

mystring_decoded = mystring.decode()
print(mystring_decoded)
print(type(mystring_decoded))

'''
	UTIL METHODS FOR STRINGS
		len: get the longitude of one object
		replace("string to replace", "string replaced"): replace one string by other.
		find: search one string in other string and checks if exists.
		strip: cuts all the spaces 
		lstrip: cuts the white spaces located in the left side one string.
		rstrip: cuts the white spaces located in the right side of one string.
		upper: converts one string into uppercase words.
		lower: converts one string into lowercase words.
		split: splits or divide a string by one separator, that could be one character.
		join: paste all characters of one string with one separator.
'''
this_string = "This is one simple string"
print(this_string)

#get the longitude
print(len(this_string)) 

#find the content in the string, and get the index
searched_index = this_string.find("w") #get minus one when the content wasn't finded
print(searched_index)

#replace in the string
replaced_string = this_string.replace("simple", "complex")
print(replaced_string)	

#delete the white spaces in one string
string = " This is one string with    spaces    "
print(string)

#delete the white spaces in the left
print(string.lstrip())

#delete the white spaces in the right
print(string.rstrip())

#delete all the spaces
print(string.strip())

#convert all to lowercas
print(string.lower())

#convert all to uppercase
print(string.upper())

#source line get separate all the lines by one
source_line = "int var1; int *p1;"
lines = source_line.split(";");
lines_splited = len(lines)-1

for line_index in range(lines_splited):
	print("{0}:{1}".format(line_index, lines[line_index].strip()))

#join the string elements
string2 = "abcdefg"
print(string2.join(";"))
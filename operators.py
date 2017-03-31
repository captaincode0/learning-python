'''
	There is different type of operators, one operator is the implementation of
	one operation that could be applied specificaly to one kind of data

				Numeric operators
	Arithmetic					Logic
								   |-- Low level operators

	The operations are overloaded and have different behavior it depends of the datatype
	that are implemented
'''

'''
	Let a and b two numbers

	Arithmetic operators
		sum => a+b
		remainder => a-b
		mult => a*b
		module => a%b
		div => a/b
		int div => a//b
		pow [a^b] => a**b
'''

a = 0b01100001 #97
b = 0b00000001 #1

result = a+b
print("The result of [a+b] is {0}".format(result))

result = a-b
print("The result of [a-b] is {0}".format(result))

result = a*a
print("The result of [a*a] is {0}".format(result))

result = a%2
print("The result of [a%2] is {0}".format(result))

result = a/(b+1)
print("The result of [a/(b+1)] is {0}".format(result))

result = a//(b+1)
print("The result of [a//(b+1)] is {0}".format(result))

result = a**2
print("The result of [a**2] is {0}".format(result))

'''
	Logic operations
		Equaly => a==b
		Unequaly => a!=b
		Or => a or b 
		And  => a and b 

		Low level operations [Bit level]
			a Or b => a | b
			a And b => a & b
			a Xor b => a ^ b
'''

result = a==b
print("The result of [a==b] is {0}".format(result))

result = a!=b
print("The result of [a!=b] is {0}".format(result))

result = a or b
print("The result of [a or b] is {0}".format(result))

result = a and b
print("The result of [a and b] is {0}".format(result))

result = a | b
print("The result of [a|b] is {0}".format(result))

result = a & b
print("The result of [a&b] is {0}".format(result))
# 0x09-python-everything_is_object

Has different txt files, each an answer to an object question

the difference between use of /* == */ and /* is */

_==_ checks for equality of the  values while _is_ checks the object 

e.g	a = "bananas"
	b = "bananas"

	a == b; True
	a is b; True

these works for immutable objects like strings, on list on the other hand
e.g	a = [1, 2, 3]
	b = [1, 2, 3]
	
	a == b; True
	a is b; False

however if you were to alias the list, b = a,
both a and b would point to the same object, just different names:
e.g 	a = [1, 2, 3]
	b = a
	print(b)
	...[1, 2, 3]
	
	b[0] = x
	print(a)
	...[x, 2, 3]
	
	b == a; True
	a is b; True

to get a copy of the list without having to alias
clone or use the copy function
e.g	a = [1, 2, 3]
	b = [:]
	print(b)
	...[1, 2, 3]
	
	b[0] = x
	print(a)
	...[1, 2, 3]
	print(b)
	...[x, 2, 3]
	
	a is b; False

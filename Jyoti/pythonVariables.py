a=10
b="Jyoti"
c=100.00
print(a,b,c)

# Assigning single value to multiple variables
x=y=z=100
print(x,y,z)

# Assigning multiple values to multiple variables
l,m,n=11,20.0,"Asha"
print(l,m,n)

#Tuples-Immutable and enclosed with parenthesis

tupleExample={10,40.0,"ITT"}
print(tupleExample)
# tupleExample[0]=50 renders error- does not support item assignment
# print(tupleExample) 

#List-Mutable and enclosed with square brackets

listExample=[10,40.0,'ITT']
print(listExample)
listExample[0]=50
print(listExample)
print(listExample[0])

#Dictionary - Key-value pair, No two keys can be same

dictionary={'a':'100','name':'Jyoti'}
print(dictionary.keys())
print(dictionary.values())




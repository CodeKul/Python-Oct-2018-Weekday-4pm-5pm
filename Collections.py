# str

var1 = 'Codekul'
print(var1)

var2 = "The Gurukul for Coders!"
print(var2)

var3 = '''Implementation
    is
        more
            important
                than learning'''

print(var3)

print("Codekul- 'Python'")
print('Codekul- "Python"')
print(''''codekul'- "Python"''')

a = 10
# Value: 10

print("Value: %d"%a)

print("Value: {}".format(a))

b = 20

print("Value of a: {}\nValue of b: {}".format(a,b))

var1 = str(10)
var2 = str(20)

print(var1 + var2)

# list
list1 = [1,2,3,4,5,6,7,8,9, 'Chetan', 12.89]
print(list1)
list1.append(10)
print(list1)

list2 = [1,2,3, ['Chetan', 'Shweta']]
list2[2] = 33
print(list2[3][0])

# tuple
t1 = (1,2,3,4,5)

# t1[2] = 33
# t1.append(6)

print(t1[3])

# dict
dict1 = {"key": "Value"}
print(dict1["key"])
dict1["Key1"] = 10
dict1[10] = "Ten"

print(dict1)
# complex

# (1 +2j)

c1 = complex(1,2)
print(c1)

c2 = complex(5,10)
print(c2)

c3 = c1 / c2
print(c3)
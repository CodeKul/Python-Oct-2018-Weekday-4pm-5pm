a = int(input('Enter intrger value of a: '))
b = int(input('Enter intrger value of b: '))
c = int(input('Enter intrger value of c: '))

max = 0
if a > b:
    if a > c:
        max = a
    else:
        max = c
else:
    if b > c:
        max = b
    else:
        max = c
print('Max: ',max)


min = 0

if a < b and a < c:
    min = a
elif b < c:
    min = b
else:
    min = c

print("Min: ",min)
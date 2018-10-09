a = 15
if a > 20:
        print("a is greater than 20")
        
print("This is outside the if")

if a == 10:
        print("a is equal to 10")
elif a < 10:
        print("a is less than 10")
else:
        print("a is greater than 10")


a = 7
if a < 10:
        if a > 5:
                print("a is in between 5 and 10")
        else:
                print("a is less than or equal to 5")
elif a > 10:
        print("a is greater than 10")
else:
        print("a is equal to 10")


# Loops

a = 0
while a < 10:
        print("Codekul- {}".format(a))
        a += 1

students = ['Prasad', 'Akash', 'Chetan', 'Amar', 'Samant', 'Shweta']
# for stu in students:
#         for ch in stu:
#                 print(ch)
#         print('\n')

for (index, name) in enumerate(students):
        print('Index: {}\nName: {}\n'.format(index, name))
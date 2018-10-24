#f=open("test.txt","w")
#f.write("This is a test")

f= open("test.txt","r")
f.seek(6,1)
name = f.readline()
f.seek(9,1)
company_name = f.readline()
f.seek(7,1)
phone = f.readline()

print(name)
print(company_name)
print(phone)

with open('list.txt') as f1:
   for line in f1:
       if 'str' in line:
          break


f1 = open("list.txt", "r")
courses = []

while True:
    f1.seek(3,1)
    line = f1.readline()
    if not line:
        break
    courses.append(line)

print(courses)
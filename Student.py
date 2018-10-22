class Student:
    def __init__(self, rno, name, marklist):
        self.rno = rno
        self.name = name
        self.marklist = marklist

    def display(self):
        print('Roll no.: {}'.format(self.rno))
        print('Name: {}'.format(self.name))
        self.marklist.display()
        
class MarkList:
    subject1 = 0
    subject2 = 0
    subject3 = 0
    subject4 = 0
    subject5 = 0

    def __init__(self, subject1, subject2, subject3, subject4, subject5):
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
        self.subject4 = subject4
        self.subject5 = subject5

    def display(self):
        print("Subject1: {}".format(self.subject1))
        print("Subject2: {}".format(self.subject2))
        print("Subject3: {}".format(self.subject3))
        print("Subject4: {}".format(self.subject4))
        print("Subject5: {}".format(self.subject5))

    def totalMarks(self):
        return self.subject1 + self.subject2 + self.subject3 + self.subject4 + self.subject5

    def percentageMarks(self):
        return (self.totalMarks()/500.0)*100

class School:
    name = ''
    students = []

    def __init__(self, name, students):
        self.name = name
        self.students = students

    def display(self):
        for stu in self.students:
            stu.display()
            print('')

    def numberOfStudents(self):
        return len(self.students)

    def averageMarksOfStudents(self):
        sum = 0.0
        for stu in self.students:
            sum += stu.marklist.percentageMarks()
        return sum/self.numberOfStudents()

    def getIntelligentStudent(self):
        maxMarks = max(stu.marklist.percentageMarks() for stu in self.students)
        for stu in self.students:
            if stu.marklist.percentageMarks() == maxMarks:
                return stu
        return None

    def getDullStudent(self):
        minMarks = min(stu.marklist.percentageMarks() for stu in self.students)
        for stu in self.students:
            if stu.marklist.percentageMarks() == minMarks:
                return stu
        return None

    
    
    
marklist1 = MarkList(90,93,89,85,75)
stu1 = Student(1, 'Chetan', marklist1)

marklist2 = MarkList(89,69,79,82,61)
stu2 = Student(2, 'Shweta', marklist2)

marklist3 = MarkList(98,59,76,93,91)
stu3 = Student(3, 'Amar', marklist3)

marklist4 = MarkList(86,87,76,95,73)
stu4 = Student(4, 'Aishwarya', marklist4)

marklist5 = MarkList(86,72,91,56,73)
stu5 = Student(5, 'Akash', marklist5)

students = [stu1, stu2, stu3, stu4, stu5]

school = School('My School',students)

school.display()

print('Average marks: {}'.format(school.averageMarksOfStudents()))

iStu = school.getIntelligentStudent()
print("Topper: {}".format(iStu.marklist.percentageMarks()))

iStu = school.getDullStudent()
print("Non Topper: {}".format(iStu.marklist.percentageMarks()))

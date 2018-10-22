class Company:
    def __init__(self, name, employees = None):
        self.name = name
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def display(self):
        print('Name: {}'.format(self.name))
        for emp in self.employees:
            emp.display()
            print('')

    def raise_salary(self):
        for emp in self.employees:
            emp.raise_salary()



class Employee(object):
    def __init__(self, first_name, last_name, id, raise_s):
        self.first_name = first_name
        self.last_name = last_name
        self.raise_s = raise_s
        self.id = id

    def display(self):
        print(self.id)
        print(self.get_full_name())
        print(self.raise_s)

    def get_full_name(self):
        return  self.first_name + ' ' + self.last_name

    def get_email(self):
        return None


class Developer(Employee):
    def __init__(self, first_name, last_name, id, raise_s, salary):
        super().__init__(first_name, last_name, id, raise_s)
        self.salary = salary
        self.email = self.get_email()

    def display(self):
        super().display()
        print(self.email)
        print(self.salary)

    def get_email(self):
        return 'dev_'+self.first_name+'.'+self.last_name+'@xyz.com'

    def raise_salary(self):
        self.salary *= self.raise_s     

class Manager(Employee):
    def __init__(self, first_name, last_name, id, raise_s, salary):
        super().__init__(first_name, last_name, id, raise_s)
        self.salary = salary
        self.email = self.get_email()

    def display(self):
        super().display()
        print(self.email)
        print(self.salary)

    def get_email(self):
        return 'man_'+self.first_name+'.'+self.last_name+'@xyz.com'

    def raise_salary(self):
        self.salary *= self.raise_s     


dev1 = Developer('Shweta', 'Chaudhari', 1, 1.2, 5000)
dev2 = Developer('Akash', 'Chavan', 2, 1.5, 3000)

man1 = Manager('Prasad', 'Lungare', 3, 1.8, 8000)
man2 = Manager('Amar', 'Singh', 4, 1.7, 9000)

company = Company('xyz', [dev1, dev2, man1, man2])

print('Before raise:')
company.display()
company.raise_salary()

print('After raise:')
company.display()
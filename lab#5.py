'''
Ryo Fujimura
Lab 5
CIS275C
'''

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def __str__(self):
        return "Name: {}, Age: {}, Address: {}".format(self.name, self.age, self.address)

class Student(Person):
    def __init__(self, name, age, address, student_id, grade_level):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grade_level = grade_level
    def __str__(self):
        return super().__str__() + ", Student ID: {}, Grade Level: {}".format(self.student_id, self.grade_level)

class Employee(Person):
    def __init__(self, name, age, address, salary, years_on_job):
        super().__init__(name, age, address)
        self.salary = salary
        self.years_on_job = years_on_job
    def __str__(self):
        return super().__str__() + ", Salary: {}, Years on Job: {}".format(self.salary, self.years_on_job)

class Faculty(Employee):
    def __init__(self, name, age, address, salary, years_on_job, faculty_id, subject):
        super().__init__(name, age, address, salary, years_on_job)
        self.faculty_id = faculty_id
        self.subject = subject
    def __str__(self):
        return super().__str__() + ", Faculty ID: {}, Subject: {}".format(self.faculty_id, self.subject)

def main():
    person = Person("John", 20, "123 Main St")
    student = Student("Jane", 18, "456 Main St", 12345, 12)
    employee = Employee("Bob", 22, "789 Main St", 500000, 10)
    faculty = Faculty("Sue", 23, "111 Main St", 600000, 15, 123, "Math")
    print(person)
    print(student)
    print(employee)
    print(faculty)

if __name__ == "__main__":
    main()

'''
Output:
Name: John, Age: 20, Address: 123 Main St
Name: Jane, Age: 18, Address: 456 Main St, Student ID: 12345, Grade Level: 12
Name: Bob, Age: 22, Address: 789 Main St, Salary: 500000, Years on Job: 10
Name: Sue, Age: 23, Address: 111 Main St, Salary: 600000, Years on Job: 15, Faculty ID: 123, Subject: Math
'''
'''
Create the following classes: Person, Employee, Faculty, and Student

Person should have:

    name
    age
    address

Student should be a subclass of Person and have:

    Student ID
    Grade Level

Employee should be a subclass of Person and have:

    Salary
    Years on the Job

Faculty should be a subclass of Employee and have:

    Faculty ID
    Subject taught

Have each class override the __str__ method, printing all of its attributes (including any inherited ones).  In your main function, demonstrate creating one of each type of object (and print each as well)
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
    employee = Employee("Bob", 40, "789 Main St", 50000, 10)
    faculty = Faculty("Sue", 35, "1011 Main St", 60000, 15, 123, "Math")
    print(person)
    print(student)
    print(employee)
    print(faculty)

if __name__ == "__main__":
    main()


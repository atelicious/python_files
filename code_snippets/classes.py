#code snippets for classes basics

class Students:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.full_name = f'{fname} {lname}'
        
    def email(self):
        return f'{self.fname}{self.lname}@company.com'

    @property
    def return_email(self):
        return f'{self.fname}{self.lname}@company.com'


#creates a student_1 instance 
student_1 = Students('test', 'student') 

print(student_1) #verifies the existence of student_1 object

#to access the objects values: object.value, where object = object created,  
#value = value instantiated in the __init__ method
print(student_1.fname)
print(student_1.lname)
print(student_1.full_name)

#to access class methods inside classes:
#call via object -> object.method(), where object = object created using the class,
#method = method inside the class

print(student_1.email())

#call via class = Class.method(object), where Class = class to be used, 
#method = method inside the Class, object = object created using the class

print(Students.email(student_1))

#access @property methods: @property methods are somewhat like vthe variables
#created using __init__ method as @property decorator turns that method into a class attribute
#to access @@propery attribute in an object: object.property

print(student_1.return_email)
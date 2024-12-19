# Parent class
class Person():
    
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name
        
    def get_name(self):
        return f"{self.first_name} {self.last_name}"
    

class Student(Person):
    # By using the super() function, you do not have to use the name of the
    # parent element, it will automatically inherit the methods and properties 
    # from its parent.

    def __init__(self, fname, lname, graduation_year=None):
    #    Person.__init__(self, fname, lname)
       super().__init__(fname, lname)
       self.graduation_year = graduation_year
       
    # Method overriding
    def get_name(self):
        return f"Name is: {self.first_name} {self.last_name}"
    
    def get_graduation_year(self):
        return f"Graduation year is: {self.graduation_year}"
    
    
x = Person("John", "Doe")
print(x.get_name())


y = Student("Mike", "Olsen", 2024)    
print(y.get_name())
print(y.get_graduation_year())
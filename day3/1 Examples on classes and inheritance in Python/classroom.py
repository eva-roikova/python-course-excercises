class Person(object):
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fullname(self):
        return self.first_name + ' ' + self.last_name

class Student(Person):
    def __init__(self,first_name,last_name,subject):
        Person.__init__(self,first_name,last_name)
        self.subject = subject

    def fullnamesubject(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.subject

class Teacher(Person):
    def __init__(self,first_name,last_name,subject):
        Person.__init__(self,first_name,last_name)

    def teachersubject(self,subject):
        return self.first_name + ' ' + self.last_name + ' ' + subject

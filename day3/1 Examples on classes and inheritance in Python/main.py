from classroom import Person
from classroom import Student
from classroom import Teacher

person1 = Person('Alex','Blunt')
FullName1 = person1.fullname()
print(FullName1)

person2 = Person('Amanda','Olivieri')
FullName2 = person2.fullname()
print(FullName2)

person3 = Student('Charllie','Lemon','geography')
FullName3_subject = person3.fullnamesubject()
print(FullName3_subject)

course = "physics"
teacher = Teacher('William','Brooks',course)

subject_teacher = teacher.teachersubject(course)
print(subject_teacher)
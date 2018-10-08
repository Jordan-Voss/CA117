from collections import namedtuple

Student = namedtuple("Student", ["firstname", "surname", "id"])

def show_student(student):
	print("First name: {}".format(student.firstname))
	print("   Surname: {}".format(student.surname))
	print("        ID: {}".format(student.id))

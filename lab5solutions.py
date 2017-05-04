""" (1) STANFORD PREREQS """

type(a) # => <class 'lab5test.Course'>
isinstance(a, Course) # => True
isinstance(b, Course) # => True
type(a) == type(b) # => False
a == b # => False

# ADDITIONAL ATTRIBUTES
class Course:
	def __init__(self, department, number, title):
		self.department = department
		self.number = number
		self.title = title
		self.students_here = set()	

	def mark_attendance(self, *students):
		for s in students:
			self.students_here.add(s)

	def is_present(self, student):
		return student in self.students_here


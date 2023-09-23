class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  #Sort the list of students in descending order of cgpa
  Sorted_Students = sorted(student_list,
                          key=lambda student: student.cgpa,
                          reverse=True)
  #syntax - lambda arg:exp
  return Sorted_Students 


#Example usage:
students = [
  Student("Hari", "A123", 7.8),
  Student("srikanth", "A124", 8.9),
  Student("Archana", "A125", 9.8),
  Student("Ram", "A126", 6.8),
]

sorted_students = sort_students(students)

#print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))





class student:
  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):

 sorted_students = sorted(student_list,key=lambda student:student.cgpa,reverse=True)
 return sorted_students



students = [
      student("Dharuni","A1234",8.8),
      student("Queen","A1235", 8.5),
      student("priya","A1236", 9.2),
      student("Arjun","A1237",9.7),
]


sorted_students = sort_students(students)
for student in sorted_students:
  print("Name: {},Roll Number: {},CGPA: {}".format(student. name,student.roll_number,       student.cgpa))



class job:
  name = None
  salary = None
  hoursWorked = None

  def __init__(self, name, salary, hoursWorked):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked

  def print(self):
    print(f"Job type: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Hours worked: {self.hoursWorked}\n")

class doctor(job):

  def __init__(self,salary,hoursWorked,experience,speciality):
    self.name = "Doctor"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.experience = experience
    self.speciality = speciality
    
  def print(self):
    print(f"Job type: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Hours worked: {self.hoursWorked}")
    print(f"Speciality: {self.speciality}")
    print(f"Years of experience: {self.experience}\n")
  

class teacher(job):

  def __init__(self,salary,hoursWorked,subject,position):
    self.name = "Teacher"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.subject = subject
    self.position = position


  def print(self):
    print(f"Job type: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Hours worked: {self.hoursWorked}")
    print(f"Subject: {self.subject}")
    print(f"Position: {self.position}\n")


print("Jobs Jobs Jobs!\n")

lawyer = job("Lawyer","$ Squillions",60)

lawyer.print()

pediatric = doctor("$ Doing very nicely thank you",50,7,"Pediatric Consultant")
pediatric.print()

ClassroomTeacher = teacher("$ Nowhere near enough","All of them","Computer Science", "Classroom Teacher")
ClassroomTeacher.print()
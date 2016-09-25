class Employee:
  'Common class for Employee'
  employeeCount = 0
  def __init__(self, name, city):
    self.name = name
    self.location = city
    Employee.employeeCount = Employee.employeeCount + 1

  def showCount(self):
    print("Total employes joined so far: " + Employee.employeeCount)

  def details(self):
    print("Name: " + self.name + "\nLocation: " +self.location)

#Demonstration
print("I have defined a class " + Employee.__name__ + \
" defined in " + Employee.__module__ + " module and " + \
"documented as \n" + Employee.__doc__)
print("Let's now run a demo.")
emp = Employee("Siddhant", "Kothrud")
emp.details()

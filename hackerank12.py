class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    def __init__(self, firstName, lastName, idNumber):
        super().__init__(firstName, lastName, idNumber)
    test_scores = []
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    
    # Write your constructor here
    

    #   Function Name: calculate
    def calculate():
	    for i in scores:
		    
    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()
test_number = input(int())
scores = input(int())
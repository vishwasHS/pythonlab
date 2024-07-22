class student:
    school_name="asd"
    def __init__(self,x,y,z):
        self.__name=x
        self.__usn=y
        self.__cgpa=z
    def display(self,x):
        if self.__usn==x:
            print("School name",student.school_name)
            print("name",self.__name)
            print("usn",self.__usn)
            print("cgpa",self.__cgpa)
    def calculate(self):
        cgpa = self.__cgpa
        
        if cgpa > 9:
            return 'O'
        elif cgpa >= 8:
            return 'A'
        elif cgpa >= 7:
            return 'B'
        elif cgpa >= 6:
            return 'C'
        elif cgpa >= 5:
            return 'D'
        elif cgpa >= 4:
            return 'P'
        else:
            return 'F'
        
    def update(self,x):
        if self.__usn==x:
            a=float(input("enter cgpa to update:"))
            self.__cgpa=a
            print("updated")
            
n=int(input("enter number of students:"))
students_list=[]
for i in range(n):
    x,y,z=input("enter name\n usn\n cgpa\n").split()
    s=student(x,y,float(z))
    students_list.append(s)
    
while True:
    choice = int(input("Enter 1 to display details, 2 to calculate grade, 3 to update CGPA, 4 to delete, 5 to exit: "))
    
    if choice == 5:
        break
    
    usn = input("Enter USN: ")
    found = False
    
    for s in students_list:
        if s._student__usn == usn:
            found = True
            if choice == 1:
                s.display(usn)
            elif choice == 2:
                print("Grade:", s.calculate())
            elif choice == 3:
                s.update(usn)
            elif choice == 4:
                students_list.remove(s)
                print("Student deleted")
            else:
                print("Invalid input")
    
    if not found:
        print("Student with USN '{}' not found.".format(usn))

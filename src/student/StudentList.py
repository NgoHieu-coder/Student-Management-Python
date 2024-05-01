import csv
from student.Student import Student

student_file_name = "data/student.csv" 

class Node:    
    def __init__(self, student):        
        self.value = student        
        self.next = None
        
    def printNode(self):
        self.value.print_student()

class StudentList:
       
    head = Node(None)
    tail = Node(None) 
    
    def __init__(self):
        self.head = self.tail = None
        
    def isEmpty(self):
        return self.head == None
    
    def addLast(self, student):
        node = Node(student)
        if self.isEmpty():
            self.tail = self.head = node
        else:
            self.tail.next = node
            self.tail = node
 
    def remove_node(self,target):
        # If the list is empty, return None
        if not self.head:
            return None

        # If the target is the head, update the head pointer
        if self.head.value == target:
            return self.head.next

        # Traverse the list to find the node before the target
        prev = self.head
        current = self.head.next
        while current:
            if current.value == target:
                # Remove the node by updating the pointers
                prev.next = current.next
                return self.head
            prev = current
            current = current.next

        # If the target is not found, return the head
        return self.head
 
    # method to make the list iterable
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next    
            
    @staticmethod
    def create_student(line):
        tokens = line.strip().split(",")
        roll = tokens[0].strip()
        name = tokens[1].strip()
        birth = int(tokens[2].strip())
        hometown = tokens[3].strip()
        return Student(roll, name, birth, hometown)
    
    def read_from_file(self):
        with open(student_file_name, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for line in csv_reader:
                student = self.create_student(",".join(line))
                self.addLast(student)  # Add student to the linked list
                
    def save_to_file(self):
        with open(student_file_name, "w") as file:
            file.write("roll,name,birth,hometown\n")
            for student in self:
                file.write(f"{student.roll},{student.name},{student.birth},{student.hometown}\n")
        print("Student data saved to file successfully.")



    def printList(self):
        print("-------------------------------------------------------------------------\n")
        print("| Roll       | Name                 | Age        | Hometown             |\n")
        print("-------------------------------------------------------------------------\n")
        for student in self:
            student.print_student()
        print("-------------------------------------------------------------------------\n")
        
    def searchByRoll(self, roll):
        found_student = None
        for student in self:
            if (student.roll == roll):
                found_student = student
                break
        return found_student

    # find by roll
    def displayByRoll(self, roll):
        find = self.searchByRoll(roll)
        if (find != None):
            print("Student Found!\n")
            find.print_student() 
        else:
            print("Not found!")
            
    def add_student(self):
        roll = input("Enter Roll: ")
        for s in self:
            if (s.roll == roll):
                print("\nThis Roll is already taken.\nPlease enter a different Roll.")
                return False
        name = input("Enter Name: ")
        birth = int(input("Enter birth year: "))
        hometown = input("Enter hometown: ")
        student = Student(roll, name, birth, hometown)
        self.addLast(student)
        print("Student added successfully.")
        return True

    def delete_student(self, roll, mark_list):
        status = False
        # find student by roll
        stud = self.searchByRoll(roll)
        if (stud == None):
            print("No such student exists.")
            return status
        # check student learnt a subject, if yes => cannot delete
        if mark_list.check_student_existence(roll) != False:
            print("This student has learnt a subject.\n Therefore, he/ she cannot be deleted")
            return status
        # remove from linked list and set status to true
        self.remove_node(stud)
        print("Student deleted successfully!")
        status = True
        return status
    
    def update_student(self, new_name, new_birth, new_hometown):
        self.name = new_name
        self.year = new_birth
        self.hometown = new_hometown
        
        roll = input("Enter the student id you want to update the profile for: ")
        if roll in Student :
            print("The student profile:")
            Student[roll].print_student()

        # edit profile
            Student[roll].update_student(new_name, new_birth, new_hometown)

            print("Student information after updating:")
            Student[roll].print_student()
        else:
            print("Invalid student information!")

                

            

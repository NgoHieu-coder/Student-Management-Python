from student.StudentList import StudentList
from subject.SubjectList import SubjectList
from mark.MarkList import MarkList
from view.menu import Menu
from controllers.main_controller import Controller
    
def main():
    student_list = StudentList()
    student_list.read_from_file()
    
    subject_list = SubjectList()
    subject_list.read_from_file()
    
    mark_list = MarkList()
    mark_list.read_from_file()
        
    status = False
    while True:
        Menu.display_main_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            status = Controller.student_management(student_list, subject_list, mark_list)
        elif choice == '2':
            status = Controller.subject_management(subject_list, mark_list)
        elif choice == '3':
            # status = grade_management(mark_list)
            pass
        elif choice == '4':
            status = Controller.save_all_file(student_list, subject_list, mark_list)
        elif choice == '5':
            Controller.exit_app(student_list, subject_list, mark_list, status)
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
22
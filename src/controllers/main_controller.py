from view.menu import Menu
class Controller:
    def study_management(roll, student_list, subject_list, mark_list):
        status = False
        while True:
            Menu.display_update_study()
            choice = input("Enter your choice: ")
            if choice == '1':
                # add new mark
                subject_list.printList()
                subject_id = input("Enter subject id: ")
                if subject_list.searchBySubjectId(subject_id) != None:
                    mark = mark_list.input_mark(roll, subject_id, None)
                    status = mark_list.add_mark(mark)
                    print("Registered successfully!")
                else:
                    print("Invalid subject!")            
            elif choice == '2':
                # update mark
                mark_list.print_student_marks(roll)
                subject_id = input("Enter subject id: ")
                if (roll, subject_id) in mark_list.marks: # check if student registered subject
                    score = input("Input new score: ")
                    mark = mark_list.input_mark(roll, subject_id, score)
                    mark_list.update_mark(mark)
                    print("Updated successfully!")
                    status = True
                else:
                    print("This student hasn't joined in this subject!")
            elif choice == '3':
                print("Student's transcript: \n")
                mark_list.print_student_marks(roll)
            elif choice == '4':
                return status

    def student_management(student_list, subject_list, mark_list):
        status = False
        while True:
            Menu.display_student_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                student_list.printList()
            elif choice == '2':
                roll = input("Enter roll number: ")
                student_list.displayByRoll(roll)
            elif choice == '3':
                status = student_list.add_student()
            elif choice == '4':
                roll = input("Enter roll number: ")
                # update profile
                student_list.update_student(roll)
                
            elif choice == '5':
                roll = input("Enter roll number: ")
                if student_list.searchByRoll(roll) != None:
                    status = Controller.study_management(roll, student_list, subject_list, mark_list)
                else:
                    print("Student not found.")
                
            elif choice == '6':
                roll = input("Enter roll number: ")
                status = student_list.delete_student(roll, mark_list)
                
            elif choice == '7':
                return status  # Return to the main menu
            else:
                print("Invalid choice. Please try again.")
            
    
    def subject_management(subject_list, mark_list):
        status = False
        while True:
            Menu.display_subject_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                subject_list.printList()
            elif choice == '2':
                id = input("Enter subject id: ")
                subject_list.displayById(id)
            elif choice == '3':
                status = subject_list.add_subject()
            elif choice == '4':
                id = input("Enter subject id: ")
                name = input("Enter new subject name: ")
                if (name.strip() != ""):
                    status = subject_list.update_subject(id, name)
            elif choice == '5':
                id = input("Enter subject id: ")
                status = subject_list.delete_subject(id, mark_list)
            elif choice == '6':
                id = input("Enter subject id: ")
                mark_list.print_subject_marks(id)
            elif choice == '7':
                return status  # Return to the main menu
            else:
                print("Invalid choice. Please try again.")
            
    def save_all_file(student_list, subject_list, mark_list):
        student_list.save_to_file()
        subject_list.save_to_file()
        mark_list.save_to_file()
        return False
    
    def exit_app(student_list, subject_list, mark_list, status):
        if status:
            confirm = input("You made some changes to the data in this system.\nDo you want to save before exit? (y/n): ")
            if confirm == 'y':
                status = Controller.save_all_file(student_list, subject_list, mark_list)
                print("Saved! Exiting...")
            else:
                print("Exiting without saving...")
        else:
            print("Exiting...")       
from module import * 

import module.AccademyRecord as p


# p.add_C(101,'java','9','10')
# p.add_C(102,'Data Structure','5' , '2')
# p.add_C(103,'Python','10', '8')
# print(p.viewCourse())


# p.delete_Course(103)
# print(p.viewCourse())

# print("The 1st Semester Result is : ", p.find_cgpa() )




def main():
    while True:
        print("\n--- Academic Performance Tracker ---")
        print("1. Add Course")
        print("2. Drop Course")
        print("3. Print Academic Record")
        print("4. Calculate CGPA")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        # Simulating switch-case with a dictionary
        switch = {
            '1': lambda: p.add_course(
                int(input("Enter student ID: ")),
                input("Enter course name: "),
                float(input("Enter total credits: ")),
                float(input("Enter earned points: "))
            ),
            '2': lambda: p.drop_course(
                int(input("Enter student ID: ")),
                input("Enter course name to drop: ")
            ),
            '3': lambda:p.print_academic_record(
                int(input("Enter student ID: "))
            ),
            '4': lambda: print(f"Current CGPA: {p.calculate_cgpa(int(input('Enter student ID: '))):.2f}"),
            '5': lambda: exit("Exiting the program.")
        }

        # Execute the selected option
        action = switch.get(choice)
        if action:
            action()
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

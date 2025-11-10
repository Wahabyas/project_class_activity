

def add_record():
    try:
        student_id = input("Enter Student ID: ").strip()
        name = input("Enter Name: ").strip()
        course = input("Enter Course: ").strip()
        grade_input = input("Enter Grade: ").strip()
        try:
            grade = float(grade_input)
        except ValueError:
            print("Invalid input! Grade must be a number.")
            return
        with open("grades.txt", "a") as file:  
            file.write(f"{student_id}, {name}, {course}, {grade}\n")
        print("Record added successfully!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def view_records():
    try:
        with open("grades.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No records found.")
                return
            print("----------------------------")
            for line in lines:
                student_id, name, course, grade = [x.strip() for x in line.split(",")]
                print(f"{student_id} | {name} | {course} | {grade}")
            print("----------------------------")

    except FileNotFoundError:
        print("No records found. The file 'grades.txt' does not exist yet.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def search_record():
    try:
        student_id_search = input("Enter Student ID to search: ").strip()

        with open("grades.txt", "r") as file:
            lines = file.readlines()

            found = False
            for line in lines:
                student_id, name, course, grade = [x.strip() for x in line.split(",")]
                if student_id == student_id_search:
                    print(f"Record found: {student_id} | {name} | {course} | {grade}")
                    found = True
                    break

            if not found:
                print("Record not found.")

    except FileNotFoundError:
        print("No records found. The file 'grades.txt' does not exist yet.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    while True:
        print("============================")
        print("    STUDENT GRADE SYSTEM")
        print("============================")
        print("[1] Add New Record")
        print("[2] View All Records")
        print("[3] Search Record by ID")
        print("[4] Exit")
        print("============================")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            search_record()
        elif choice == "4":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1–4.")


if __name__ == "__main__":
    main()

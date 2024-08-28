'''
                                    EXPERIMENT - 9
'''
class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Marks (Physics, Chemistry, Maths):", self.marks)

    def percentage(self):
        total_marks = sum(self.marks)
        percentage = (total_marks / (len(self.marks) * 100)) * 100
        return percentage

    def display_result(self):
        marks_percentage = self.percentage()
        result = "Pass" if all(mark >= 40 for mark in self.marks) else "Fail"       #if any subject is below than 40 --> fail
        print("Result:", result)
        print("Marks Percentage:", marks_percentage)

def average_class(students):
    total_percentage = sum(student.percentage() for student in students)
    avg_percentage = total_percentage / len(students)
    return avg_percentage

# Example usage
def main():
    n = 3 
    students = []
    for i in range(n):
        name = input("Enter student name: ")
        sap_id = input("Enter SAP ID: ")
        marks = [int(input("Enter Physics marks: ")),
                 int(input("Enter Chemistry marks: ")),
                 int(input("Enter Maths marks: "))]
        students.append(Student(name, sap_id, marks))

    print("\nDetails of all students:")                                         # Display details of all students
    for student in students:
        student.display()
        student.display_result()
        print()

    # Average marks of the class
    print("Average marks of the class:", average_class(students))


if __name__ == "__main__":
    main()

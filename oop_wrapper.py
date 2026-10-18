
# Employee Management System - OOP Wrapper

# Person class (parent of Employee)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# ---------------------------------------------------------
# Employee class (Base class)
# employee_id and salary are PRIVATE (encapsulation)
# ---------------------------------------------------------
class Employee(Person):
    
    def __init__(self, name, age, employee_id="Not set", salary=0.0):
        super().__init__(name, age)          
        self.__employee_id = employee_id     
        self.__salary = float(salary)        

    # Getter and setter for employee_id
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter and setter for salary
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = float(salary)

    def display(self):
        super().display()                    
        print("Employee ID:", self.__employee_id)
        print("Salary: $" + str(self.__salary))

    
    def __del__(self):
        print("Cleaning up:", self.name)


# ---------------------------------------------------------
# Manager class (Derived class)
# ---------------------------------------------------------
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    
    def display(self):
        super().display()
        print("Department:", self.department)


# ---------------------------------------------------------
# Developer class (Derived class)
# ---------------------------------------------------------
class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print("Programming Language:", self.programming_language)


# ---------------------------------------------------------
# Helper functions to read numbers safely
# ---------------------------------------------------------
def read_age():
    while True:
        try:
            return int(input("Enter Age: "))
        except ValueError:
            print("Please enter a whole number.")


def read_salary():
    while True:
        try:
            return float(input("Enter Salary: "))
        except ValueError:
            print("Please enter a number.")


# ---------------------------------------------------------
# Menu-driven user interface
# ---------------------------------------------------------
def show_menu():
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")


def main():
    print("--- Python OOP Project: Employee Management System ---")

    print("Manager is a subclass of Employee:", issubclass(Manager, Employee))
    print("Developer is a subclass of Employee:", issubclass(Developer, Employee))

    person = None
    employee = None
    manager = None

    while True:
        show_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("\nEnter Name: ")
            age = read_age()
            person = Person(name, age)
            print("\nPerson created with name: " + name + " and age: " + str(age) + ".")

        elif choice == "2":
            name = input("\nEnter Name: ")
            age = read_age()
            emp_id = input("Enter Employee ID: ")
            salary = read_salary()
            employee = Employee(name, age, emp_id, salary)
            print("\nEmployee created with name: " + name + ", age: " + str(age)
                  + ", ID: " + emp_id + ", and salary: $" + str(float(salary)) + ".")

        elif choice == "3":
            name = input("\nEnter Name: ")
            age = read_age()
            emp_id = input("Enter Employee ID: ")
            salary = read_salary()
            department = input("Enter Department: ")
            manager = Manager(name, age, emp_id, salary, department)
            print("\nManager created with name: " + name + ", age: " + str(age)
                  + ", ID: " + emp_id + ", salary: $" + str(float(salary))
                  + ", and department: " + department + ".")

        elif choice == "4":
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            detail = input("Enter your choice: ")

            if detail == "1":
                if person is None:
                    print("\nNo Person has been created yet.")
                else:
                    print("\nPerson Details:")
                    person.display()
            elif detail == "2":
                if employee is None:
                    print("\nNo Employee has been created yet.")
                else:
                    print("\nEmployee Details:")
                    employee.display()
            elif detail == "3":
                if manager is None:
                    print("\nNo Manager has been created yet.")
                else:
                    print("\nManager Details:")
                    manager.display()
            else:
                print("\nInvalid choice.")

        elif choice == "5":
            print("\nExiting the system. All resources have been freed.")

            del person, employee, manager
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")

        print("\n--- Choose another operation ---")

main()

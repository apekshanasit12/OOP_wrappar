# Employee Management System (OOP Wrapper)

A beginner-friendly Python project that uses **Object-Oriented Programming (OOP)** to model people, employees and managers. You use it through a simple text menu in the console.

---

## Table of Contents

- [About](#about)
- [Project Requirements](#project-requirements)
- [OOP Concepts Used](#oop-concepts-used)
- [Classes](#classes)
- [Getting Started](#getting-started)
- [How to Use](#how-to-use)
- [Example Run](#example-run)
- [Project Structure](#project-structure)
- [Assumptions](#assumptions)

---

## About

The goal of this project is to practise OOP by building a small Employee Management System. The program lets you create different kinds of people (a Person, an Employee or a Manager) and then view their details from a menu.

## Project Requirements

**Project:** OOP Wrapper

**Objective:** The goal of this project is to build an Employee Management System that utilizes various Object-Oriented Programming (OOP) concepts like classes, inheritance, encapsulation, method overloading, method overriding, and more. The system will model employee data and operations related to adding, updating, and removing employees, as well as tracking their roles (e.g., Manager, Developer).

### Project Structure & Requirements

**Employee Class (Base Class):**
- The Employee class should have attributes such as employee_id, name, age, and salary.
- Provide getter and setter methods for salary and employee_id.
- Define a constructor to initialize these attributes and a destructor to clean up resources.
- Use self to refer to instance attributes.

**Manager Class (Derived Class):**
- Inherits from Employee.
- Additional Attribute: Adds a new attribute department (e.g., HR, Finance).
- Override display() to include department information.

**Developer Class (Derived Class):**
- Inherits from Employee.
- Additional Attribute: Adds a new attribute programming_language (e.g., Python, Java).
- Override display() to include programming language information.

**Method Overloading:**
- Provide different constructors in the Employee class to allow multiple ways of creating employee objects.

**Encapsulation:**
- Encapsulate sensitive data like salary and employee_id by making them private and providing getter and setter methods.

**Inheritance and Method Overriding:**
- Use inheritance to create specialized classes like Manager and Developer.
- Override the display() method to include specific details.

**Use of super() and issubclass():**
- Use super() to call the parent class methods.
- Use issubclass() to check if a class is a subclass of Employee class.

**User Interface (UI):**
- Create a menu-driven interface to let users choose from different options.
- Allow users to exit the program from the main menu.

### Submission Requirements

- Make suitable assumptions wherever necessary and document them in the project documentation or README.md file.
- Create a GitHub repository to host the project. Upload the project files, including source code, and documentation, with a clear and descriptive README.md file.
- Do not copy code or any other content from classmates or any other source. All code and content must be original and properly attributed to the appropriate sources, if applicable.
- Submit the GitHub repository link to your instructor or as instructed.

## OOP Concepts Used

| Concept | How it is used in this project |
|---|---|
| **Classes and objects** | `Person`, `Employee`, `Manager` (and `Developer`) are classes. Each person you create is an object. |
| **Constructor** (`__init__`) | Sets up each object's attributes when it is created. |
| **Destructor** (`__del__`) | Cleans up when an object is removed. This is why the program says "All resources have been freed" when you exit. |
| **Encapsulation** | Sensitive data like `salary` and `employee_id` is private and is accessed only through getter and setter methods. |
| **Inheritance** | `Employee` builds on `Person`. `Manager` and `Developer` build on `Employee`. |
| **Method overriding** | `Manager` and `Developer` change the `display()` method to show their extra information. |
| **Method overloading** | `Employee` can be created in more than one way (different constructor options). |
| **`super()`** | Lets a child class call its parent class's methods. |
| **`issubclass()`** | Checks whether a class is a subclass of `Employee`. |
| **`self`** | Used to refer to an object's own attributes. |

## Classes

- **Person**: has a `name` and an `age`.
- **Employee** (inherits from Person): adds `employee_id` and `salary`, with getters and setters for both.
- **Manager** (inherits from Employee): adds a `department`, for example HR, Finance or Sales.
- **Developer** (inherits from Employee): adds a `programming_language`, for example Python or Java.

## Getting Started

### What You Need

- [Python 3](https://www.python.org/downloads/) installed on your computer

To check, open a terminal and type:

```bash
python --version
```

### Installation

1. Download the project:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. Go into the project folder:

   ```bash
   cd your-repo-name
   ```

No extra libraries are needed. The project only uses Python's built-in features.

## How to Use

Run the program:

```bash
python main.py
```

You will see a menu. Type the number of the option you want and press Enter:

```
Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit
```

| Option | What it does |
|---|---|
| **1** | Asks for a name and age, then creates a Person. |
| **2** | Asks for a name, age, employee ID and salary, then creates an Employee. |
| **3** | Asks for the same details as an Employee plus a department, then creates a Manager. |
| **4** | Lets you choose Person, Employee or Manager and prints that object's details. |
| **5** | Exits the program and frees all resources. |

After each action, the menu appears again until you choose **5**.

## Example Run

```
--- Python OOP Project: Employee Management System ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit

Enter your choice: 2

Enter Name: Jane Smith
Enter Age: 28
Enter Employee ID: E123
Enter Salary: 50000

Employee created with name: Jane Smith, age: 28, ID: E123, and salary: $50000.0.

--- Choose another operation ---

Enter your choice: 3

Enter Name: Alice Johnson
Enter Age: 40
Enter Employee ID: M456
Enter Salary: 80000
Enter Department: Sales

Manager created with name: Alice Johnson, age: 40, ID: M456, salary: $80000.0, and department: Sales.

Enter your choice: 4

Choose details to show:
1. Person
2. Employee
3. Manager
Enter your choice: 2

Employee Details:
Name: Jane Smith
Age: 28
Employee ID: E123
Salary: $50000.0

Enter your choice: 5

Exiting the system. All resources have been freed.
Goodbye!
```

## Project Structure

```
your-repo-name/
├── README.md    # This file
└── main.py      # The program: classes and the menu
```

> Update the file names above to match your own project files.

## Assumptions

These are the assumptions made while building this project:

- The program runs in the console and takes input from the keyboard.
- Age is entered as a whole number, and salary is entered as a number.
- Salary is displayed as a decimal with a `$` sign (for example `$50000.0`).
- Employee IDs are text (for example `E123`, `M456`).
- The menu lets you create a Person, an Employee and a Manager. The `Developer` class is included to demonstrate inheritance and overriding, even though it is not in the menu.
- Only the most recently created object of each type is shown under "Show Details".
- Data is kept in memory only. Nothing is saved after the program exits.
- The user enters valid menu choices (1 to 5).

## Author

APEKSHA

Course / Assignment: PR. 5 OOP Wrapper# OOP_wrappar

# exercises_oop_day2.py

"""
OOP Bootcamp — Day 2 Exercises
Each exercise focuses on a fundamental concept in object-oriented programming (OOP).
"""

# ========== Exercise 1: Define a Simple Teacher Class ==========
# Goal: Understand the basics of class creation and instantiation
# The teacher has to have a first name, a last name, an age, and a list of subjects to teach
# All these attributes can be used in a class 'def teach(self):...'

class Teacher:
    def __init__(self, first_name, last_name, age, subjects):

    def teach(self):

# CHALLENGE: Create two teachers with different subjects and call their `teach()` method.


# ========== Exercise 2: Object Comparison and String Representation ==========
# Goal: Implement __str__ and __eq__ methods

class Student:
    def __init__(self, first_name, last_name, birth_year):

    def __str__(self):

    def __eq__(self, other):

# CHALLENGE: Create two students. Compare them. Print them.


# ========== Exercise 3: Encapsulation and Properties ==========
# Goal: Control access and validation for attributes

class Course:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
            print(f"{student.first_name if hasattr(student, 'first_name') else student} added to {self.name}")
        else:
            print(f"Cannot add {student.first_name if hasattr(student, 'first_name') else student}: {self.name} is full")

    def list_students(self):
        for s in self.students:
            print("-", s)

# CHALLENGE: Create a course with capacity 2, add 3 students, increase the capacity, then try again.


# ========== Exercise 4: Inheritance ==========
# Goal: Create a class hierarchy and reuse behavior

class Animal:
    def __init__(self, name):
        self.name = name
        self.death_probability = 0

    def __str__(self):
        return f"{self.name} (Death %: {self.death_probability})"

    def cry(self):
        raise NotImplementedError("Each animal must define its own cry.")

class Cat(Animal):
    def __init__(self, name, fur_type):
        super().__init__(name)
        self.fur_type = fur_type
        self.death_probability = 0.5

    def cry(self):
        print("Meow")

class Dog(Animal):
    def __init__(self, name, is_trained):
        super().__init__(name)
        self.is_trained = is_trained
        self.death_probability = 1

    def cry(self):
        print("Woof")

# CHALLENGE: Create a list of animals. Call their cry() method in a loop.


# ========== Exercise 5: Advanced — A School System ==========
# Goal: Combine all concepts into a larger system

class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def hire_teacher(self, teacher):
        self.teachers.append(teacher)

    def enroll_student(self, student):
        self.students.append(student)

    def list_people(self):
        print(f"--- {self.name} ---")
        print("Teachers:")
        for t in self.teachers:
            print("-", t.first_name, t.last_name)
        print("Students:")
        for s in self.students:
            print("-", s)

# CHALLENGE:
# 1. Create 1 school, 2 teachers, 3 students
# 2. Enroll and hire them
# 3. Print the school roster

# Bonus CHALLENGE:
# Add a system where students can be expelled or transfer to another school


if __name__ == "__main__":
    print("Run this file section by section while debugging to understand how OOP works in Python.")
    print("Each class is a standalone example — build and test each one in order.")


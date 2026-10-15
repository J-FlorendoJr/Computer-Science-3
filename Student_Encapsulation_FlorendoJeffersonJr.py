class Student:

    # Constructor
    def __init__(self, name, age, grade):
        self.name = name
        self.__age = age
        self.__grade = grade

    # Getter for age
    def get_age(self):
        return self.__age

    # Getter for grade
    def get_grade(self):
        return self.__grade

    # ================================================
    # TASK 1: COMPLETE THE AGE SETTER
    # ================================================
    # Requirements:
    # - Accept ages greater than or equal to 0.
    # - Reject negative ages.
    # - Print "Invalid age!" for invalid values.
    # - Retain the previous age if input is invalid.

    def set_age(self, age):
        # WRITE YOUR CODE BELOW
        if age > 0:
             self.__age = age
        else:
            print("Invalid age!")


    # ================================================
    # TASK 2: COMPLETE THE GRADE SETTER
    # ================================================
    # Requirements:
    # - Accept grades from 0 to 100 (inclusive).
    # - Reject grades below 0 or above 100.
    # - Print "Invalid grade!" for invalid values.
    # - Retain the previous grade if input is invalid.

    def set_grade(self, grade):
        # WRITE YOUR CODE BELOW
        if grade > 0 and grade <= 100:
            self.__grade = grade
        else:
            print("Invalid Grade!")


# =====================================================
# TASK 3: TEST YOUR PROGRAM
# =====================================================

# Create a student object
student1 = Student("Alex", 15, 90)

# Display original values
print("Original Student Information")
print("Name:", student1.name)
print("Age:", student1.get_age())
print("Grade:", student1.get_grade())


# TEST 1: Change age to 16
# Expected: Age becomes 16
student1.set_age(16)
print("\nTest 1 - Age:", student1.get_age())


# TEST 2: Change age to -5
# Expected: "Invalid age!" and age remains 16
student1.set_age(-5)
print("Test 2 - Age:", student1.get_age())


# TEST 3: Change grade to 95
# Expected: Grade becomes 95
student1.set_grade(95)
print("\nTest 3 - Grade:", student1.get_grade())


# TEST 4: Change grade to 150
# Expected: "Invalid grade!" and grade remains 95
student1.set_grade(150)
print("Test 4 - Grade:", student1.get_grade())


# TEST 5: Change grade to 0
# Expected: Grade becomes 0
student1.set_grade(0)
print("\nTest 5 - Grade:", student1.get_grade())

# =====================================================
# REFLECTION QUESTION
# =====================================================
# Answer in 2-3 sentences:
#
# Why is it important to use setter methods instead
# of allowing unrestricted modification of an
# object's attributes?
print("\nYOUR ANSWER: It's important because setters allow private attributes to be protected, encapsulated, and be validated.")
#
#
#
# =====================================================
# CHECKLIST
# =====================================================
# [/] Completed set_age() method
# [/] Completed set_grade() method
# [/] Executed all five test cases
# [/] Verified the expected output
# [/] Answered the reflection question
# [/] Saved and submitted the completed Python file
#
# END OF ACTIVITY
# =====================================================
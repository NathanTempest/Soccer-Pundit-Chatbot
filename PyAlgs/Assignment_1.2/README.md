# Assignment 1.2: Control Statements and Program Development

This project contains Python programs solving five basic exercises designed to teach logic flow, control structures (conditionals and loops), and error handling using try-except blocks.

---

## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Running the Code
To run any of the exercises, navigate to this directory in your terminal and execute the corresponding script:

```bash
# Exercise 1: Name and Welcome
python3 ex_1.py

# Exercise 2: Gross Pay Computation
python3 ex_2.py

# Exercise 3: Gross Pay with Try/Except Error Handling
python3 ex_3.py

# Exercise 4: Score Grading Program
python3 ex_4.py

# Exercise 5: Password Loop Validation
python3 ex_5.py
```

---

## Exercise Details and Pseudocode

### Exercise 1: Name and Welcome
Prompts the user for their name and outputs a personalized greeting.

* **Code File**: [ex_1.py](file:///Users/nate/Development/Python/PyAlgs/Assignment_1.2/ex_1.py)
* **Pseudocode**:
  1. Prompt the user to enter their name using the `input()` function.
  2. Store the user's input in a variable called `name`.
  3. Print "Hello" followed by a space and the value of the `name` variable.

---

### Exercise 2: Gross Pay Computation
Prompts the user for hours worked and hourly rate, then computes the gross pay.

* **Code File**: [ex_2.py](file:///Users/nate/Development/Python/PyAlgs/Assignment_1.2/ex_2.py)
* **Pseudocode**:
  1. Prompt the user to enter the number of hours worked.
  2. Convert the input to a floating-point number and store in a variable named `hours`.
  3. Prompt the user to enter the hourly rate.
  4. Convert the input to a floating-point number and store in a variable named `rate`.
  5. Compute the gross pay by multiplying the `hours` by the `rate`.
  6. Print the computed gross pay prefixed by "Pay: ".

---

### Exercise 3: Gross Pay with Try/Except Error Handling
Improves the gross pay computation program by checking for non-numeric inputs using try-except.

* **Code File**: [ex_3.py](file:///Users/nate/Development/Python/PyAlgs/Assignment_1.2/ex_3.py)
* **Pseudocode**:
  1. Begin a `try` block:
     a. Prompt the user for hours worked and convert to float.
     b. Prompt the user for the hourly rate and convert to float.
     c. Compute the gross pay by multiplying hours and rate.
     d. Print the computed gross pay.
  2. Begin an `except` block to catch conversion errors (ValueError):
     a. Print "Error, please enter numeric input".
     b. Terminate the program.

---

### Exercise 4: Score Grading Program
Prompts for a score between 0.0 and 1.0, checks for bounds/errors, and outputs the letter grade.

* **Code File**: [ex_4.py](file:///Users/nate/Development/Python/PyAlgs/Assignment_1.2/ex_4.py)
* **Pseudocode**:
  1. Prompt the user to enter a score.
  2. Begin a `try` block:
     a. Convert the input to a floating-point number.
     b. Check if the score is less than 0.0 or greater than 1.0. If so, print "Bad score".
     c. Otherwise (score is valid), check the score range:
        - If score >= 0.9, print "A"
        - Else if score >= 0.8, print "B"
        - Else if score >= 0.7, print "C"
        - Else if score >= 0.6, print "D"
        - Else (score < 0.6), print "F"
  3. Begin an `except` block (if conversion to float fails):
     a. Print "Bad score".

---

### Exercise 5: Password Loop Validation
Prompts the user for a password repeatedly until the correct password is provided.

* **Code File**: [ex_5.py](file:///Users/nate/Development/Python/PyAlgs/Assignment_1.2/ex_5.py)
* **Pseudocode**:
  1. Set the correct password value to "python123".
  2. Initialize an infinite loop (`while True`).
  3. Prompt the user to enter a password.
  4. If the entered password matches "python123":
     a. Print "Access granted!".
     b. Exit/break the loop.
  5. If the entered password does not match:
     a. Print "Incorrect password. Try again." and let the loop continue.

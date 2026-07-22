# Assignment 2.2: Sequences, Functions, and Descriptive Statistics

This directory contains Python programs and a dynamically compiled APA-formatted MS Word report for the 5 exercises of Assignment 2.2.

---

## Files

1. **[ex_1.py](file:///Users/nate/Development/Python/PyAlgs/Assignment_2.2/ex_1.py)**: Prints the current date and time using `datetime`.
2. **[ex_2.py](file:///Users/nate/Development/Python/PyAlgs/Assignment_2.2/ex_2.py)**: Prints a conversion chart showing Celsius and Fahrenheit equivalents in range 0–100 degrees.
3. **[ex_3.py](file:///Users/nate/Development/Python/PyAlgs/Assignment_2.2/ex_3.py)**: Performs slice operations on string `alphabet` containing `'abcdefghijklmnopqrstuvwxyz'`.
4. **[ex_4.py](file:///Users/nate/Development/Python/PyAlgs/Assignment_2.2/ex_4.py)**: Filters a list of tuples containing first and last names, outputting tuples containing the last name "Jones".
5. **[ex_5.py](file:///Users/nate/Development/Python/PyAlgs/Assignment_2.2/ex_5.py)**: Calculates frequencies and descriptive statistics (min, max, range, mean, median, mode, sample variance, sample standard deviation) for 20 survey responses.
6. **[generate_doc.py](file:///Users/nate/Development/Python/PyAlgs/Assignment_2.2/generate_doc.py)**: Programmatically constructs the final APA-formatted report.
7. **[Jason_Nathaniel_Assignment_2_2.docx](file:///Users/nate/Development/Python/PyAlgs/Assignment_2.2/Jason_Nathaniel_Assignment_2_2.docx)**: The generated APA Word report containing the title page, introduction, exercises, reflections, and references.

---

## Execution Steps

### Prerequisites
Install necessary libraries:
```bash
python3 -m pip install docx numpy pandas --user
```

### Running Exercises
To execute any individual script, run:
```bash
python3 ex_1.py
python3 ex_2.py
python3 ex_3.py
python3 ex_4.py
python3 ex_5.py
```

### Generating the MS Word Report
To compile the final report, execute:
```bash
python3 generate_doc.py
```
This will compile the APA report and overwrite/create `Jason_Nathaniel_Assignment_2_2.docx` in the same directory.

# Messy Python Code Improvement (AI-Assisted Refactoring)

A student coursework demonstration of identifying bad practices in beginner Python code and refactoring it into clean, maintainable, PEP 8-compliant code using AI assistance.

- **Author**: Ayan Khan (Enrolment No: `25BCON1174`)
- **Institution**: Department of Computer Science & Engineering, JECRC University
- **GitHub Repository**: [https://github.com/ayankhanbebea-lgtm/messy-python-code-improvement](https://github.com/ayankhanbebea-lgtm/messy-python-code-improvement)

---

## 1. Project Background
In 2nd-year computer science coursework, initial code drafts often prioritize "just getting the answer to print" over structure, reusability, and readability. This project takes an authentic student scenario—calculating academic grades, averages, and attendance eligibility across multiple students—and demonstrates how to systematically improve it using modern AI refactoring techniques.

Both versions are preserved in this repository for direct before-and-after comparison.

---

## 2. Issues in the Messy Version (`messy_grade_calculator.py`)

| Defect Category | Example in Messy Code | Problem / Engineering Risk |
|:---|:---|:---|
| **Cryptic Variable Naming** | `s1_n`, `s1_m`, `t1`, `a1`, `g1`, `st1` | Difficult to read, understand, or maintain. Requires reader to decipher meaning. |
| **DRY Violation (Code Duplication)** | Same loop & `if/elif` blocks copy-pasted 3+ times | Violates "Don't Repeat Yourself". Adding a 5th student requires copy-pasting 30 lines. Any bug fix must be manually repeated everywhere. |
| **Monolithic Script Structure** | No user-defined functions | Logic cannot be imported, unit tested, or reused across modules. |
| **Hardcoded Global Scope** | Everything in flat root execution | Pollutes global namespace and makes test assertions impossible. |
| **Absence of Data Validation** | Division `t1 / len(s1_m)` without empty check | Raises `ZeroDivisionError` if a student has no submitted assignments. |
| **Manual String Concatenation** | `"Total: " + str(t1) + " Average: " + str(a1)` | Inefficient, verbose, and difficult to format cleanly. |

---

## 3. Improvements in the Clean Version (`clean_grade_calculator.py`)

1. **Modular Function Decomposition**:
   - `determine_grade(average_score)`: Pure function mapping percentage to letter grades.
   - `check_attendance_eligibility(attendance_percentage)`: Verifies university 75% attendance criteria.
   - `process_student_record(student_dict)`: Computes individual total, mean, grade, and eligibility.
   - `generate_class_report(students_list)`: Calculates aggregate metrics (class average, eligible count, top performer).
   - `display_report(report)`: Formats output into a readable terminal summary.

2. **Structured Data Modeling**:
   - Uses list of standardized dictionaries representing structured records. Easily scalable to 5, 50, or 5,000 students.

3. **Type Hints & Documentation**:
   - Python 3 type hints (`List[float]`, `Dict[str, Any]`, `Optional`) and standard docstrings for clarity.

4. **Defensive Edge-Case Handling**:
   - Gracefully handles empty marks lists without crashing.

5. **Automated Verification Tests**:
   - Built-in `run_tests()` function using assertions to guarantee correctness across boundary conditions (90%, 80%, 75% attendance threshold, etc.).

---

## 4. Before vs. After Code Comparison

### Before (Messy Snippet):
```python
# Copy-pasted for every student
t1 = 0
for x in s1_m:
    t1 = t1 + x
a1 = t1 / len(s1_m)
if a1 >= 90:
    g1 = "A+"
elif a1 >= 80:
    g1 = "A"
...
```

### After (Clean & Reusable):
```python
def determine_grade(average_score: float) -> str:
    """Determine letter grade based on standard percentage thresholds."""
    if average_score >= 90.0:
        return "A+"
    elif average_score >= 80.0:
        return "A"
    elif average_score >= 70.0:
        return "B"
    elif average_score >= 60.0:
        return "C"
    elif average_score >= 50.0:
        return "D"
    return "F"
```

---

## 5. How AI Assistance Was Applied
Cursor AI / Large Language Models were leveraged to:
1. **Smell Detection**: Analyze the script for code smells (PEP 8 non-compliance, duplicate blocks, unhandled edge cases).
2. **Decomposition Guidance**: Suggest breaking monolithic code into single-responsibility functions.
3. **Test Generation**: Formulate test cases covering boundary conditions (75.0% vs 74.9% attendance, grade breakpoints).

---

## 6. How to Run

### Run the Original Messy Script:
```bash
python messy_grade_calculator.py
```

### Run the Clean Version (Includes Automated Unit Tests):
```bash
python clean_grade_calculator.py
```

### Expected Output of Clean Version:
```text
============================================================
           ACADEMIC PERFORMANCE & ATTENDANCE REPORT
============================================================
Roll: 101  | Name: Rahul Sharma      
      Total: 406.0  | Avg: 81.20  | Grade: A  
      Attendance: 82.0% (Eligible)
------------------------------------------------------------
Roll: 102  | Name: Priya Patel       
      Total: 468.0  | Avg: 93.60  | Grade: A+ 
      Attendance: 91.0% (Eligible)
------------------------------------------------------------
...
============================================================
                     CLASS SUMMARY
============================================================
Total Enrolled Students : 4
Overall Class Average   : 65.65%
Exam Eligible Students  : 2 / 4
Top Performer           : Priya Patel (93.6% - Grade A+)
============================================================

Running Verification Test Suite:
All unit tests passed successfully!
```

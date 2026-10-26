"""Student Grade & Attendance Tracker.

Refactored Clean Version (AI-Assisted Improvement).
Demonstrates:
- Clean modular functions with single responsibility
- Type hints and descriptive variable naming
- Proper data modeling using dictionaries / records
- Robust input validation and edge-case handling (empty marks, invalid attendance)
- Automated verification test suite
"""

from typing import List, Dict, Any, Optional


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


def check_attendance_eligibility(attendance_percentage: float, minimum_required: float = 75.0) -> bool:
    """Check whether a student meets the minimum attendance requirement."""
    return attendance_percentage >= minimum_required


def process_student_record(student: Dict[str, Any]) -> Dict[str, Any]:
    """Process academic marks and attendance for a single student record."""
    name = student.get("name", "Unknown")
    roll_number = student.get("roll_number", 0)
    marks: List[float] = student.get("marks", [])
    attendance = float(student.get("attendance", 0.0))

    if not marks:
        total = 0.0
        average = 0.0
        grade = "N/A"
    else:
        total = sum(marks)
        average = total / len(marks)
        grade = determine_grade(average)

    is_eligible = check_attendance_eligibility(attendance)

    return {
        "name": name,
        "roll_number": roll_number,
        "marks_count": len(marks),
        "total": round(total, 2),
        "average": round(average, 2),
        "grade": grade,
        "attendance": attendance,
        "attendance_status": "Eligible" if is_eligible else "Low Attendance",
    }


def generate_class_report(students: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Compute aggregate class statistics across all student records."""
    if not students:
        return {
            "processed_students": [],
            "total_students": 0,
            "class_average": 0.0,
            "eligible_count": 0,
            "top_performer": None,
        }

    processed = [process_student_record(s) for s in students]
    class_avg = sum(p["average"] for p in processed) / len(processed)
    eligible_count = sum(1 for p in processed if p["attendance_status"] == "Eligible")
    top_performer = max(processed, key=lambda p: p["average"])

    return {
        "processed_students": processed,
        "total_students": len(processed),
        "class_average": round(class_avg, 2),
        "eligible_count": eligible_count,
        "top_performer": top_performer,
    }


def display_report(report: Dict[str, Any]) -> None:
    """Print a clean, formatted text report for terminal viewing."""
    print("=" * 60)
    print("           ACADEMIC PERFORMANCE & ATTENDANCE REPORT")
    print("=" * 60)

    for student in report["processed_students"]:
        print(f"Roll: {student['roll_number']:<4} | Name: {student['name']:<18}")
        print(f"      Total: {student['total']:<6} | Avg: {student['average']:<6.2f} | Grade: {student['grade']:<3}")
        print(f"      Attendance: {student['attendance']}% ({student['attendance_status']})")
        print("-" * 60)

    print("\n" + "=" * 60)
    print("                     CLASS SUMMARY")
    print("=" * 60)
    print(f"Total Enrolled Students : {report['total_students']}")
    print(f"Overall Class Average   : {report['class_average']:.2f}%")
    print(f"Exam Eligible Students  : {report['eligible_count']} / {report['total_students']}")
    if report["top_performer"]:
        top = report["top_performer"]
        print(f"Top Performer           : {top['name']} ({top['average']}% - Grade {top['grade']})")
    print("=" * 60)


def run_tests() -> None:
    """Automated unit verification tests for clean grade calculator."""
    # Test 1: Grade thresholds
    assert determine_grade(95.0) == "A+"
    assert determine_grade(85.0) == "A"
    assert determine_grade(75.0) == "B"
    assert determine_grade(65.0) == "C"
    assert determine_grade(55.0) == "D"
    assert determine_grade(45.0) == "F"

    # Test 2: Attendance eligibility
    assert check_attendance_eligibility(75.0) is True
    assert check_attendance_eligibility(74.9) is False
    assert check_attendance_eligibility(90.0) is True

    # Test 3: Record processing
    sample = {"name": "Test Student", "roll_number": 999, "marks": [80, 90], "attendance": 80}
    res = process_student_record(sample)
    assert res["total"] == 170.0
    assert res["average"] == 85.0
    assert res["grade"] == "A"
    assert res["attendance_status"] == "Eligible"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    students_database = [
        {"name": "Rahul Sharma", "roll_number": 101, "marks": [78, 85, 90, 65, 88], "attendance": 82},
        {"name": "Priya Patel",  "roll_number": 102, "marks": [92, 95, 89, 94, 98], "attendance": 91},
        {"name": "Aman Verma",   "roll_number": 103, "marks": [45, 52, 48, 40, 50], "attendance": 68},
        {"name": "Sneha Gupta",  "roll_number": 104, "marks": [35, 28, 42, 30, 39], "attendance": 55},
    ]

    report = generate_class_report(students_database)
    display_report(report)
    print("\nRunning Verification Test Suite:")
    run_tests()

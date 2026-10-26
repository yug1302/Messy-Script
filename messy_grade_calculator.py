# Student Grade & Attendance Tracker
# Original Messy Version (Beginner/Draft Code)
# Issues: Cryptic single-letter variables, repeated logic, hardcoded values,
# no input validation, lack of modular functions, and unhandled division by zero.

s1_n = "Rahul Sharma"
s1_r = 101
s1_m = [78, 85, 90, 65, 88]
s1_att = 82

s2_n = "Priya Patel"
s2_r = 102
s2_m = [92, 95, 89, 94, 98]
s2_att = 91

s3_n = "Aman Verma"
s3_r = 103
s3_m = [45, 52, 48, 40, 50]
s3_att = 68

s4_n = "Sneha Gupta"
s4_r = 104
s4_m = [35, 28, 42, 30, 39]
s4_att = 55

# Calculate student 1
t1 = 0
for x in s1_m:
    t1 = t1 + x
a1 = t1 / len(s1_m)
if a1 >= 90:
    g1 = "A+"
elif a1 >= 80:
    g1 = "A"
elif a1 >= 70:
    g1 = "B"
elif a1 >= 60:
    g1 = "C"
elif a1 >= 50:
    g1 = "D"
else:
    g1 = "F"

if s1_att >= 75:
    st1 = "Eligible"
else:
    st1 = "Low Attendance"

print("--- STUDENT 1 ---")
print("Name: " + s1_n)
print("Roll: " + str(s1_r))
print("Total: " + str(t1))
print("Average: " + str(a1))
print("Grade: " + g1)
print("Attendance: " + str(s1_att) + "% (" + st1 + ")")

# Duplicate logic for student 2
t2 = 0
for x in s2_m:
    t2 = t2 + x
a2 = t2 / len(s2_m)
if a2 >= 90:
    g2 = "A+"
elif a2 >= 80:
    g2 = "A"
elif a2 >= 70:
    g2 = "B"
elif a2 >= 60:
    g2 = "C"
elif a2 >= 50:
    g2 = "D"
else:
    g2 = "F"

if s2_att >= 75:
    st2 = "Eligible"
else:
    st2 = "Low Attendance"

print("\n--- STUDENT 2 ---")
print("Name: " + s2_n)
print("Roll: " + str(s2_r))
print("Total: " + str(t2))
print("Average: " + str(a2))
print("Grade: " + g2)
print("Attendance: " + str(s2_att) + "% (" + st2 + ")")

# Duplicate logic for student 3
t3 = 0
for x in s3_m:
    t3 = t3 + x
a3 = t3 / len(s3_m)
if a3 >= 90:
    g3 = "A+"
elif a3 >= 80:
    g3 = "A"
elif a3 >= 70:
    g3 = "B"
elif a3 >= 60:
    g3 = "C"
elif a3 >= 50:
    g3 = "D"
else:
    g3 = "F"

if s3_att >= 75:
    st3 = "Eligible"
else:
    st3 = "Low Attendance"

print("\n--- STUDENT 3 ---")
print("Name: " + s3_n)
print("Roll: " + str(s3_r))
print("Total: " + str(t3))
print("Average: " + str(a3))
print("Grade: " + g3)
print("Attendance: " + str(s3_att) + "% (" + st3 + ")")

# Class average calculation
all_avg = (a1 + a2 + a3) / 3
print("\n====================")
print("Class Average: " + str(all_avg))

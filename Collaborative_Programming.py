# --- TASK: Calculating for Current grade ---
SA1 = float(input("Enter your SA1 grade: "))
SA2 = float(input("Enter your SA2 grade: "))
FA1 = float(input("Enter your FA1 grade: "))
FA2 = float(input("Enter your FA2 grade: "))
SA = (SA1 + SA2) / 2
FA = (FA1 + FA2) / 2
Q4 = (SA * 0.70) + (FA * 0.30)

# --- TASK: Get the previous grade from quarter 1-3 and calculate for the final grade ---
Q1 = float(input("Enter your tentative grade for Quarter 1: "))
Q2 = float(input("Enter your tentative grade for Quarter 2: "))
Q3 = float(input("Enter your tentative grade for Quarter 3: "))

Q2_final = (Q1 + 2 * Q2) / 3
Q3_final = (Q2_final + 2 * Q3) / 3
Q4_final = (Q3_final + 2 * Q4) / 3

# --- TASK: Determine the status of the scholar based on the final grade ---
if Q4_final >= 96:
    print("Grade equivalent: 1.00")
    print("Status: EXCELLENT!")
elif Q4_final >= 90:
    print("Grade equivalent: 1.25")
    print("Status: VERY GOOD!")
elif Q4_final >= 84:
    print("Grade equivalent: 1.50")
    print("Status: VERY GOOD!")
elif Q4_final >= 78:
    print("Grade equivalent: 1.75")
    print("Status: GOOD!")
elif Q4_final >= 72:
    print("Grade equivalent: 2.00")
    print("Status: GOOD!")
elif Q4_final >= 66:
    print("Grade equivalent: 2.25")
    print("Status: SATISFACTORY!")
elif Q4_final >= 60:
    print("Grade equivalent: 2.50")
    print("Status: SATISFACTORY!")
elif Q4_final >= 54:
    print("Grade equivalent: 2.75")
    print("Status: FAIR!")
elif Q4_final >= 50:
    print("Grade equivalent: 3.00")
    print("Status: FAIR!")
elif Q4_final >= 40:
    print("Grade equivalent: 4.00")
    print("Status: FAILED ON CONDITION. . .")
else:
    print("Grade equivalent: 5.00")
    print("Status: FAILED. . .")    

# --- GRADING COMPUTATION COMPLETED ! ---
print("--- SCHOLAR SUMMARY ---")
print("Current Grade:", Q4)
print("Final Grade:", Q4_final)
print("Grading Computation COMPLETED")

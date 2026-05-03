GRADE_TABLE = [
    (96, "1.00", "EXCELLENT"),
    (90, "1.25", "VERY GOOD"),
    (84, "1.50", "VERY GOOD"),
    (78, "1.75", "GOOD"),
    (72, "2.00", "GOOD"),
    (66, "2.25", "SATISFACTORY"),
    (60, "2.50", "SATISFACTORY"),
    (54, "2.75", "FAIR"),
    (50, "3.00", "FAIR"),
    (40, "4.00", "FAILED ON CONDITION"),
]

def get_grade(score):
    for threshold, gwa, status in GRADE_TABLE:
        if score >= threshold:
            return gwa, status
    return "5.00", "FAILED"

def safe_float(prompt, lo=0, hi=100):
    while True:
        try:
            val = float(input(prompt))
            if lo <= val <= hi:
                return val
            print(f"  Please enter a value between {lo} and {hi}.")
        except ValueError:
            print("  Invalid input. Please enter a number.")

def main():
    print("=== GRADE CALCULATOR ===\n")

    # --- Q4 Current Grade ---
    SA1 = safe_float("Enter your SA1 grade: ")
    SA2 = safe_float("Enter your SA2 grade: ")
    FA1 = safe_float("Enter your FA1 grade: ")
    FA2 = safe_float("Enter your FA2 grade: ")

    SA = (SA1 + SA2) / 2
    FA = (FA1 + FA2) / 2
    Q4 = (SA * 0.70) + (FA * 0.30)

    # --- Convert Q4 score to GWA ---
    Q4_gwa, status = get_grade(Q4)

    # --- Previous Quarter GWAs ---
    print()
    Q1 = safe_float("Enter your GWA for Quarter 1 (e.g. 1.00, 1.25): ", lo=1.00, hi=5.00)
    Q2 = safe_float("Enter your GWA for Quarter 2 (e.g. 1.00, 1.25): ", lo=1.00, hi=5.00)
    Q3 = safe_float("Enter your GWA for Quarter 3 (e.g. 1.00, 1.25): ", lo=1.00, hi=5.00)

    # --- Final GWA (average of all 4 quarters) ---
    final_gwa = (Q1 + Q2 + Q3 + float(Q4_gwa)) / 4

    # --- Determine final status ---
    # Re-derive status from final_gwa by reversing the GWA to a label
    gwa_to_status = {gwa: stat for _, gwa, stat in GRADE_TABLE}
    gwa_to_status["5.00"] = "FAILED"
    
    # Round final_gwa to nearest GWA step
    valid_gwas = ["1.00", "1.25", "1.50", "1.75", "2.00", "2.25", "2.50", "2.75", "3.00", "4.00", "5.00"]
    rounded_gwa = min(valid_gwas, key=lambda g: abs(float(g) - final_gwa))
    final_status = gwa_to_status[rounded_gwa]

    # --- Summary ---
    print(f"\n--- SCHOLAR SUMMARY ---")
    print(f"  Current Grade (Q4) : {Q4:.2f}")
    print(f"  Q4 GWA             : {Q4_gwa}")
    print(f"  Quarter 1 GWA      : {Q1:.2f}")
    print(f"  Quarter 2 GWA      : {Q2:.2f}")
    print(f"  Quarter 3 GWA      : {Q3:.2f}")
    print(f"  Final GWA          : {rounded_gwa}")
    print(f"  Status             : {final_status}")
    print("\nGrading Computation COMPLETED")

main()

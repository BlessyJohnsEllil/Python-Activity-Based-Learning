maths = int(input("Enter Maths marks: "))
python = int(input("Enter Python marks: "))
english = int(input("Enter English marks: "))

if (maths < 0 or maths > 100 or
    python < 0 or python > 100 or
    english < 0 or english > 100):
    print("Invalid marks")
else:
    maths_grace = 0
    python_grace = 0
    english_grace = 0

    if 35 <= maths < 40:
        maths_grace = 40 - maths

    if 35 <= python < 40:
        python_grace = 40 - python

    if 35 <= english < 40:
        english_grace = 40 - english

    maths_final = min(maths + maths_grace, 100)
    python_final = min(python + python_grace, 100)
    english_final = min(english + english_grace, 100)

    if maths_final >= 40:
        maths_result = "Pass"
    else:
        maths_result = "Fail"

    if python_final >= 40:
        python_result = "Pass"
    else:
        python_result = "Fail"

    if english_final >= 40:
        english_result = "Pass"
    else:
        english_result = "Fail"

    print("\n--- EXAMINATION RESULT ---")
    print("Maths: Original =", maths, "Grace =", maths_grace,
          "Final =", maths_final, maths_result)
    print("Python: Original =", python, "Grace =", python_grace,
          "Final =", python_final, python_result)
    print("English: Original =", english, "Grace =", english_grace,
          "Final =", english_final, english_result)

    if (maths_final >= 40 and python_final >= 40
            and english_final >= 40):
        print("Final Result: PASS")
    else:
        print("Final Result: FAIL")

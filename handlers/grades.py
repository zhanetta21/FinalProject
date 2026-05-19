def calculate_total(regmid, regend, final):
    total = (regmid * 0.3) + (regend * 0.3) + (final * 0.4)
    return round(total, 2)

def calculate_needed_score(regmid, regend, target):
    current_score = (regmid * 0.3) + (regend * 0.3)
    needed_final = (target - current_score) / 0.4
    if needed_final <= 0:
        return 0
    return round(needed_final, 2)

def get_grade_status(total):
    if total >= 90:
        return "A - Excellent"
    elif total >= 80:
        return "B - Good"
    elif total >= 70:
        return "C - Satisfactory"
    elif total >= 50:
        return "D - Passed"
    else:
        return "F - Failed"

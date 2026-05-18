def calculate_total(regmid, regend, final):
    total = regmid + regend + final
    return round(total, 2)


def calculate_needed_score(regmid, regend, target):
    current_score = regmid + regend
    needed = target - current_score

    if needed <= 0:
        return 0

    return round(needed, 2)


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
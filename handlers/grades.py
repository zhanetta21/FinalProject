def calculate_total(regmid, regend, final):
    return regmid + regend + final


def calculate_needed_score(regmid, regend, target):
    current_score = regmid + regend
    needed = target - current_score

    if needed <= 0:
        return 0

    return needed

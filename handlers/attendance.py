def calculate_attendance(total_classes, missed_classes):
    attended = total_classes - missed_classes
    attendance = (attended / total_classes) * 100
    return round(attendance, 2)


def calculate_allowed_absences(total_classes, missed_classes, minimum_percent=70):
    max_missed = total_classes - (total_classes * minimum_percent / 100)
    allowed_left = int(max_missed - missed_classes)

    if allowed_left < 0:
        return 0

    return allowed_left

def classify_duration(minutes):
    """Validate a duration and return its study-length category."""
    if type(minutes) is not int or not 1 <= minutes <= 240:
        raise ValueError("Duration must be a whole number from 1 to 240 minutes.")

    if minutes < 30:
        return "Short"
    if minutes < 60:
        return "Medium"
    return "Long"


def create_study_record(subject, minutes):
    """Validate input and prepare a record for storage."""
    if not isinstance(subject, str) or not subject.strip():
        raise ValueError("Subject cannot be empty.")

    return {
        "subject": subject.strip(),
        "minutes": minutes,
        "category": classify_duration(minutes),
    }
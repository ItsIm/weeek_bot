import re


def check_priority(user_message: str) -> str or int:
    if user_message.startswith("!"):
        splitted_text = user_message.split(" ")
        priority = len(splitted_text[0])

        return priority
    else:
        return -1


def check_date(user_message: str) -> str or None:
    date_pattern = r'\b\d{2}\.\d{2}\.\d{4}\b'
    match = re.search(date_pattern, user_message)
    return match.group(0) if match else None


def check_time(user_message: str) -> str or None:
    time_pattern = r'\b\d{2}:\d{2}\b'
    match = re.search(time_pattern, user_message)
    return match.group(0) if match else None
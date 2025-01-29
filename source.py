def check_priority(user_message: str):
    if user_message.startswith("!"):
        splitted_text = user_message.split(" ")
        priority = len(splitted_text[0])

        return priority
    else:
        return -1


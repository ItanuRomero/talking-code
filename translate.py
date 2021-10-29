import first_level


def code_cleaner(text: str, level: int):
    if level == 0:
        code = first_level.delimiter_cleaner(text)
    elif level == 1:
        code = text
    elif level == 2:
        code = text
    return code



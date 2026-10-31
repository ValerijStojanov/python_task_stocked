def return_correct_text(text: str) -> str | bool:
    result: str = ""

    text_without_digits: str = remove_digits(text)

    if text.startswith("!"):
        result = remove_vowels(text_without_digits)
    else:
        result = text_without_digits

    text_length = len(result)

    if text_length > 140:
        return False
    else:
        return result


def remove_digits(text: str) -> str:
    result_text = ""

    for chars in text:
        if not chars.isdigit():
            result_text += chars

    return result_text


def remove_vowels(text: str) -> str:
    vowels: set[str] = {
        "a",
        "á",
        "e",
        "é",
        "ě",
        "i",
        "í",
        "o",
        "ó",
        "u",
        "ú",
        "ů",
        "y",
        "ý",
    }

    result_text: str = ""

    for chars in text:
        if chars.lower() not in vowels:
            result_text += chars

    return result_text


print(return_correct_text(input("Váš text prosím: ")))

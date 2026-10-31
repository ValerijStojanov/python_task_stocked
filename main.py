def return_correct_text(text: str) -> str | bool:
    result: str = ""

    if text.startswith("!"):
        result = remove_vowels(text)
    else:
        result = remove_digits(text)

    return result


def remove_digits(text: str) -> str:
    result_text = ""

    for chars in text:
        if not chars.isdigit():
            result_text += chars

    return result_text


def remove_vowels(text: str) -> str:
    return "Text začíná !"


print(return_correct_text(input("Váš text prosím:")))

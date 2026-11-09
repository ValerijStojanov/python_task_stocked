from main import return_correct_text

test_texts = {
    "basic_text": "Ahoj!",
    "exclamation_start": "!Ahoj",
    "digits": "Ahoj123",
    "exclamation_with_digits": "!Ahoj123",
    "czech_diacritics": "PŘÍLIŠ123",
    "exclamation_czech": "!PŘÍLIŠ123",
    "only_digits_with_exclamation": "!123",
    "only_exclamation": "!",
    "empty_text": "",
    "only_digits": "123456789",
    "uppercase_text": "AHOJ SVĚTE!",
    "uppercase_with_exclamation": "!AHOJ SVĚTE!",
    "exactly_140_chars": "b" * 140,
    "over_140_chars": "b" * 141,
    "140_chars_after_removing_digits": "123" + "b" * 140,
    "double_exclamation": "!!Ahoj123",
}


for test_name, test_input in test_texts.items():
    test_result = return_correct_text(test_input)
    print(f"{test_name}: {test_result!r}")

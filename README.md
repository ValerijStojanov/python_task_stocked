# Zpracování textu – vstupní úloha

Implementace funkce v jazyce Python pro úpravu textového řetězce podle zadaných pravidel.

## Požadavky

- Python 3.10 nebo novější
- Testováno s Pythonem 3.14.10
- Bez externích knihoven

## Pravidla zpracování textu

Funkce `return_correct_text()` přijímá textový řetězec a vrací upravený text podle následujících pravidel:

1. Z textu se vždy odstraní všechny číslice.
2. Pokud vstupní text začíná vykřičníkem (`!`):
   - Úvodní vykřičník se odstraní.
   - Odstraní se také všechny samohlásky, včetně českých samohlásek s diakritikou a jejich velkých variant.
3. Pokud délka výsledného textu po úpravách přesahuje 140 znaků, funkce vrátí logickou hodnotu `False`.
4. V ostatních případech funkce vrátí upravený řetězec.

## Struktura projektu

```text
python_task/
├── main.py
├── README.md
└── .gitignore
```

## Spuštění

```bash
python main.py
```

Skript vyzve k zadání textu a vypíše návratovou hodnotu funkce.


## Implementace

- `return_correct_text()` – hlavní funkce pro zpracování textu a kontrolu jeho délky.
- `remove_digits()` – odstranění číslic.
- `remove_vowels()` – odstranění samohlásek včetně české diakritiky.
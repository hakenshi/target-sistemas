def letter_counter(frase: str):
    counter = 0
    frase_lower = frase.lower()

    for _ in frase_lower:
        if "a" in frase_lower:
            counter+=1
        else:
            return f'A frase não possuí caracteres A.'

    return f'A frase {frase} tem {counter} letras "A"'


def main():
    print(letter_counter("banana"))


if __name__ == "main":
    main()

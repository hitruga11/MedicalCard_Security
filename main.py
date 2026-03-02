def caesar_cipher(text, shift, mode='encrypt'):
    # чтобы расшифровать просто инвертируем сдвиг
    if mode == 'decrypt':
        shift = -shift

    result = ""
    for char in text:

        result += chr(ord(char) + shift)
    return result


def main():
    print("Система MedicalCard")
    password = input("Введите пароль: ")
    key = 5

    # Шифруем
    encrypted = caesar_cipher(password, key)
    print(f"Зашифровано: {encrypted}")

    # Расшифровываем
    decrypted = caesar_cipher(encrypted, key, 'decrypt')
    print(f"Исходный вид: {decrypted}")


if __name__ == "__main__":
    main()

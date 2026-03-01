def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    #режим decrypt меняем направление сдвига
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        # Обрабатываем только печатные символы ASCII от 32 до 126
        # Это позволяет шифровать и буквы и цифры и спецсимволы
        start_pos = 32
        range_len = 95  # Количество печатных символов

        new_char = chr((ord(char) - start_pos + shift) % range_len + start_pos)
        result += new_char
    return result


def main():
    print("Система защиты пароля MedicalCard")
    password = input("Введите пароль пользователя: ")
    key = 5  # ключ сдвига

    # Шифрование
    encrypted = caesar_cipher(password, key, 'encrypt')
    print(f"Зашифрованный пароль: {encrypted}")

    # Расшифровка
    decrypted = caesar_cipher(encrypted, key, 'decrypt')
    print(f"Расшифрованный обратно: {decrypted}")


if __name__ == "__main__":
    main()

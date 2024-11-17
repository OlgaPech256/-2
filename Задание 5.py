import random


def generate_slot_machine_number() -> str:
    """Генерирует трехзначное число, имитируя игровой аппарат.

    Returns:
        str: Сгенерированное трехзначное число.
    """
    # Генерируем три случайные цифры от 0 до 9
    digits = [str(random.randint(0, 9)) for _ in range(3)]

    # Объединяем цифры в строку
    slot_number = ''.join(digits)

    return slot_number


# Пример использования
if __name__ == "__main__":
    print(generate_slot_machine_number())  # Пример: '345'
    print(generate_slot_machine_number())  # Пример: '012'
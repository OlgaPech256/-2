import random
import string


def generate_password(n: int = 8) -> str:
    """Генерирует случайный пароль заданной длины.

    Args:
        n (int): Длина пароля (по умолчанию 8).

    Returns:
        str: Сгенерированный пароль.
    """
    # Определяем алфавит
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits

    # Проверка на допустимую длину пароля
    if n > len(alphabet):
        raise ValueError(f"Длина пароля не может превышать {len(alphabet)} символов.")

    # Генерируем пароль
    password = ''.join(random.sample(alphabet, n))

    return password


# Пример использования
if __name__ == "__main__":
    print(generate_password())  # Пример: 'A1bC3dEf'
    print(generate_password(12))  # Пример: '1A2bC3dD4eE'
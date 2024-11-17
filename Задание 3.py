from typing import List, Any


def remove(lst: List[Any], value: Any) -> List[Any]:
    """Удаляет последнее вхождение значения из списка.

    Args:
        lst (List[Any]): Список, из которого нужно удалить значение.
        value (Any): Значение, которое нужно удалить.

    Returns:
        List[Any]: Измененный список.

    Raises:
        ValueError: Если значение не найдено в списке.
    """
    try:
        # Находим индекс последнего вхождения значения
        index = len(lst) - 1 - lst[::-1].index(value)
        # Удаляем элемент по найденному индексу
        lst.pop(index)
        return lst
    except ValueError:
        raise ValueError(f"Значение '{value}' не найдено в списке.")


# Пример использования
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 2, 5]
    print(remove(my_list, 2))  # Вывод: [1, 2, 3, 4, 5]

    # Пример, когда значение отсутствует
    try:
        print(remove(my_list, 10))  # Это вызовет ValueError
    except ValueError as e:
        print(e)  # Вывод: Значение '10' не найдено в списке.
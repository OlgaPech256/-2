# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter=','):
    """
    Функция для поиска общих участников двух групп.

    :param group1: Строка с фамилиями участников первой группы
    :param group2: Строка с фамилиями участников второй группы
    :param delimiter: Разделитель, по умолчанию запятая
    :return: Список общих участников, отсортированный в алфавитном порядке
    """
    # Разделяем строки на списки участников
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))

    # Находим общих участников
    common_participants = participants1.intersection(participants2)

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(group1, group2)
print(common)  # Вывод: ['Петров', 'Сидоров']

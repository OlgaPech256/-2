import csv
import json


def csv_to_json(csv_file_path, delimiter=',', line_terminator='\n'):
    # Список для хранения всех записей
    json_data = []

    # Открываем CSV файл и читаем его
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        # Создаем объект reader с заданным разделителем
        reader = csv.DictReader(csv_file, delimiter=delimiter)

        # Проходим по каждой строке в CSV и добавляем словарь в json_data
        for row in reader:
            json_data.append(row)

    # Преобразуем список словарей в JSON строку
    json_output = json.dumps(json_data, indent=4, ensure_ascii=False)

    return json_output


# Пример использования
csv_file_path = 'data.csv'  # Укажите путь к вашему CSV файлу
json_result = csv_to_json(csv_file_path)

# Печатаем результат
print(json_result)
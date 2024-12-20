import json

def sum_of_products(json_file_path):
    total_sum = 0.0

    # Открываем JSON файл и читаем его содержимое
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        # Проходим по каждому словарю в списке
        for entry in data:
            score = entry.get("score", 0)  # Получаем значение по ключу "score"
            weight = entry.get("weight", 0)  # Получаем значение по ключу "weight"
            total_sum += score * weight  # Вычисляем произведение и добавляем к общей сумме

    # Округляем сумму до 3 знаков после запятой
    return round(total_sum, 3)

# Пример использования
json_file_path = 'data.json'  # Укажите путь к вашему JSON файлу
result = sum_of_products(json_file_path)

# Печатаем результат
print(result)
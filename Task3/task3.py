import json

def generate_report(values_file, tests_file, report_file):
    """
    Генерирует отчет на основе результатов тестов и структуры отчета.

    Args:
        values_file: Путь к файлу с результатами тестов.
        tests_file: Путь к файлу со структурой отчета.
        report_file: Путь к файлу для записи отчета.
    """

    with open(values_file, 'r') as f:
        values = json.load(f)['values']
        values_dict = {item['id']: item['value'] for item in values}

    with open(tests_file, 'r') as f:
        report_structure = json.load(f)

    def fill_values(data, values_dict):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, dict):
                    fill_values(value, values_dict)
                elif isinstance(value, list):
                    for item in value:
                        fill_values(item, values_dict)
                else:
                    if key == 'id' and value in values_dict:
                        data['value'] = values_dict[value]

    fill_values(report_structure, values_dict)

    with open(report_file, 'w') as f:
        json.dump(report_structure, f, indent=2)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Неверное количество аргументов. Ожидается три пути к файлам.")
        sys.exit(1)
    generate_report(*sys.argv[1:])

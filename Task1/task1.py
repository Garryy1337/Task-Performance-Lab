import sys

def circular_array_path(n, m):
    # Создаем круговой массив
    circular_array = list(range(1, n + 1))
    
    # Начинаем с первого элемента
    current_index = 0
    path = []
    
    while True:
        # Добавляем текущий элемент в путь
        path.append(circular_array[current_index])
        
        # Вычисляем следующий индекс
        current_index = (current_index + m) % n
        
        # Если вернулись к началу, выходим из цикла
        if current_index == 0:
            break
    
    return path

if __name__ == "__main__":
    # Проверяем количество аргументов
    if len(sys.argv) != 3:
        print("Неверное количество аргументов. Ожидается два числа: n и m.")
        sys.exit(1)

    # Читаем аргументы командной строки
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    # Получаем путь и выводим его
    result_path = circular_array_path(n, m)
    print(''.join(map(str, result_path)))

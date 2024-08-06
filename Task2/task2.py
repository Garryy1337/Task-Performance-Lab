import sys

def read_circle_data(filename):
    with open(filename, 'r') as file:
        # Считываем координаты центра и радиус
        center_x, center_y = map(float, file.readline().strip().split())
        radius = float(file.readline().strip())
    return (center_x, center_y, radius)

def read_points_data(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points

def check_point_position(center, radius, point):
    center_x, center_y = center
    point_x, point_y = point
    
    # Вычисляем квадрат расстояния от центра до точки
    distance_squared = (point_x - center_x) ** 2 + (point_y - center_y) ** 2
    radius_squared = radius ** 2

    if distance_squared < radius_squared:
        return 1  # Точка внутри окружности
    elif distance_squared == radius_squared:
        return 0  # Точка на окружности
    else:
        return 2  # Точка снаружи окружности

if __name__ == "__main__":
    # Проверяем количество аргументов
    if len(sys.argv) != 3:
        print("Использование: python script.py <circle_file> <points_file>")
        sys.exit(1)

    # Читаем данные из файлов
    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    center_x, center_y, radius = read_circle_data(circle_file)
    points = read_points_data(points_file)

    # Проверяем положение каждой точки и выводим результат
    for point in points:
        position = check_point_position((center_x, center_y), radius, point)
        print(position)

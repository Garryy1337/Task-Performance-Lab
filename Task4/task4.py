import sys
from statistics import median

def min_moves(nums):
    """
    Вычисляет минимальное количество ходов для приведения всех элементов к одному числу.

    Args:
        nums: Список целых чисел.

    Returns:
        Минимальное количество ходов.
    """
    target = median(nums)
    return sum(abs(num - target) for num in nums)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Необходимо указать путь к файлу с числами.")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        nums = [int(line.strip()) for line in f]

    result = int(min_moves(nums))
    print(result)

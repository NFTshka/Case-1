def sum_negative_between_min_max(arr):
    if not arr or len(arr) < 3:
        return 0  # Между минимумом и максимумом нет элементов

    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))

    start = min(min_index, max_index) + 1
    end = max(min_index, max_index)

    # Суммируем только отрицательные элементы между min и max
    return sum(x for x in arr[start:end] if x < 0)

# Пример использования
A = [3, -5, 7, -2, 8, -1, 6, -4]
result = sum_negative_between_min_max(A)
print("Сумма отрицательных элементов между минимальным и максимальным:", result)

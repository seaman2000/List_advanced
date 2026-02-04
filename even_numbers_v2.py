list_of_numbers = list(map(int, input().split(", ")))

even_numbers = [num for num in list_of_numbers if num % 2 == 0]

print(even_numbers)
list_of_numbers = input().split(", ")

even_numbers_list = list(map(int, list_of_numbers))
result = filter(lambda x: x % 2 == 0, even_numbers_list)

print(list(result))
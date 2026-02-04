list_of_numbers = input().split(", ")

even_numbers_list = list(map(int, list_of_numbers))
even_number_indices = [idx for idx in range(len(even_numbers_list)) if even_numbers_list[idx] % 2 == 0]

print(even_number_indices)
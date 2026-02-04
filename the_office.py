def happiness_calc(list_, factor_):

    happiness_multiplied = list(map(lambda num: num * factor_, list_))
    average_happiness = sum(happiness_multiplied) / len(happiness_multiplied)
    happy_employees = [num for num in happiness_multiplied if num >= average_happiness]

    if len(happy_employees) >= 3:
        return f"Score: {len(happy_employees)}/{len(list_)}. Employees are happy!"
    else:
        return f"Score: {len(happy_employees)}/{len(list_)}. Employees are not happy!"


list_of_happiness = list(map(int, input().split()))
factor = int(input())

result = happiness_calc(list_of_happiness, factor)

print(result)

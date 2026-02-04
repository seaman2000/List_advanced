notes = [0] * 10

while True:
    command = input()
    if command == "End":
        break
    split_note = command.split("-")
    priority = int(split_note[0]) - 1
    note = split_note[1]
    notes.pop(priority)
    notes.insert(priority, note)

result = [element for element in notes if element != 0]
print(result)

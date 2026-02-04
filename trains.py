number_of_trains = [0] * int(input())

while True:
    command = input().split()
    current_command = command[0]

    if current_command == "add":
        number_of_passengers = int(command[1])
        number_of_trains[-1] += number_of_passengers

    elif current_command == "insert":
        idx = int(command[1])
        number_of_passengers = int(command[2])
        number_of_trains[idx] += number_of_passengers

    elif current_command == "leave":
        idx = int(command[1])
        number_of_passengers = int(command[2])
        number_of_trains[idx] -= number_of_passengers

    elif current_command == "End":
        print(number_of_trains)
        break
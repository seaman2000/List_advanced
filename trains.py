number_of_trains = [0] * int(input())

while True:
    command = input().split()
    current_command = command[0]
    people = int(command[2])
    if current_command == "add":
        number_of_trains[::-1] += int(command[1])
    elif current_command == "insert":
        number_of_trains.insert(int(command[1]), people)
    elif current_command == "leave":
        number_of_trains[int(command[1])] -= people
    elif command == "End":
        print("")

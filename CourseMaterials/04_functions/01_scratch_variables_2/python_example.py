def play_madlibs():
    name = input("Enter a name: ")
    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")

    print(name, "got eaten by a", adjective, animal)


def do_times_tables():
    starting_number = input("Enter a number: ")
    for mult in range(1, 12):
        print(int(starting_number) * mult)



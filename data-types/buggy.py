def do_stuff():
    tasks = ["clean", "cook", "advertise"]
    print(tasks[0])
    print(format_todos(tasks))

    # this line suprises me a lot
    print(tasks[0])


def format_todos(tasks):
    tasks.sort()
    return " - ".join(tasks)

do_stuff()
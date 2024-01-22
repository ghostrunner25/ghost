class task2:
    def __init__(self):
        pass
    def greater(self, arg):
        def is_monotonic(arg):
            return all(arg[i] <= arg[i + 1] for i in range(len(arg) - 1))


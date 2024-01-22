import itertools
class User:
    def addMoney(self, amount):
        self.money += amount

    def __repr__(self):
        return str(self.money)

    def __lt__(self, other):
        return self.money < other.money

    def __eq__(self, other):
        return self.money == other.money

    def __gt__(self, other):
        return self.money > other.money

    def __ge__(self, other):
        return self.money >= other.money

    def __le__(self, other):
        return self.money <= other.money


    userId = itertools.count()
    def __init__(self):
        self.id = next(User.userId)
        self.balance = 0
    def __str__(self):
        return f'User ID {self.id}'

    def addMoney(self, nom, count):
        def increase_balance(nom, count):
            pass
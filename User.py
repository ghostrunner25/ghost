import itertools
class User:
    '''
    Модифицировать класс таким образом, чтобы для объектов
    работал следующий код:
    users = [User(), User(), User(), User(), User(), User()]
    import random
    for user in users:
        user.addMoney(random.randint(0, 100000))
    print(max(users))
    '''
    userId = itertools.count()
    def __init__(self):
        self.id = next(User.userId)
        self.balance = 0
    def __str__(self):
        return f'User ID {self.id}'

    def addMoney(self, nom, count):
        '''
        :param nom: номинал
        :param count: количество купюр
        метод должен увеличить баланс пользователя
        '''
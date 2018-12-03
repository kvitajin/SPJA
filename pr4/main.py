class Dog:
    def __init__(self, name):
        self.name=name
    def make_sound(self):
        return '{}: Haf!'.format(self.name)
class Cat:
    def __init__(self, name):
        self.name=name
    def make_sound(self):
        return '{}: Meow!'.format(self.name)
animals=[Dog('Lassie'), Cat('Tom'), Dog('Buldog')]

for animal in animals:
    print(animal.make_sound())

# slido evenr C264
import datetime

def logger(f):
    def wrapped(*args, **kw):
        print(datetime.datetime.now())
        f(*args, **kw)
        print(datetime.datetime.now())
    return wrapped
@logger('mz logging prefix')
def test_fun(greetings):
    print('this takes really long ' + greetings)

test_fun('hello')

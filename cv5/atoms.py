import playground
import random

class Atom(object):
    x=0
    y=0
    radius=0
    rychlost_x=0
    rychlost_y=0

    def __init__(self, x, y, rychlost_x, rychlost_y, radius):
        self.x = x
        self.y = y
        self.rychlost_x=rychlost_x
        self.rychlost_y=rychlost_y
        self.radius = radius

    def to_tuple(self):
        return (self.x, self.y, self.radius)


class ExampleWorld(object):

    def __init__(self, size_x, size_y, num):
        self.width = size_x
        self.height = size_y
        self.pole = [Atom(80, 50, 5, 5, 10).to_tuple(), Atom(150, 200, 10, 10, 20).to_tuple(), Atom(100, 30,15, 15, 50).to_tuple()]
        self.num=num

    def tick(self):
        """This method is called by playground. Sends a tuple of atoms to rendering engine.
        
        :param size_x: world size x dimension
        :param size_y: world size y dimension
        :return: tuple of atom objects, each containing (x, y, radius) coordinates 
        """

        return (self.pole)


if __name__ == '__main__':
    size_x, size_y, num = 400, 300, 10

    world = ExampleWorld(size_x, size_y, num)
    n=0
    while n<world.num:
        world.pole.append(Atom(random.randint(20, 370), random.randint(20, 270), random.randint(1, 20), random.randint(0,20), random.randint(5, 50)).to_tuple())
        n+=1


    playground.run((size_x, size_y), world)





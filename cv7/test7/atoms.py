import playground
import random
#import something
import xml.etree.ElementTree as ET



class Atom(object):
    def __init__(self, pos_x, pos_y, speed_x, speed_y, size, color):
        self.pos_x = float(pos_x)
        self.pos_y = float(pos_y)
        self.size = float(size)
        self.speed_x = float(speed_x)
        self.speed_y = float(speed_y)
        self.color = color

    def to_tuple(self):
        return (self.pos_x, self.pos_y, self.size, self.color)

    def move(self, width, height):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        if self.pos_x + self.size > width:
            self.speed_x = -self.speed_x
            self.pos_x = width - self.size
        if self.pos_x < self.size:
            self.speed_x = -self.speed_x
            self.pos_x = self.size

        if self.pos_y + self.size > height:
            self.speed_y = -self.speed_y
            self.pos_y = height - self.size
        if self.pos_y < self.size:
            self.speed_y = -self.speed_y
            self.pos_y = self.size


class FallDownAtom(Atom):
    g = 3.0
    damping = 0.8
    
    def __init__(self, pos_x, pos_y, speed_x, speed_y, size, color):
        Atom.__init__(self, pos_x, pos_y, speed_x, speed_y, size, color)
    
    def move(self, width, height):
        self.speed_y += FallDownAtom.g
        
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

        if self.pos_x + self.size > width:
            self.speed_x = -self.speed_x
            self.pos_x = width - self.size
        if self.pos_x < self.size:
            self.speed_x = -self.speed_x
            self.pos_x = self.size

        if self.pos_y + self.size > height:
            self.speed_x = self.speed_x*FallDownAtom.damping
            self.speed_y = self.speed_y*FallDownAtom.damping
            self.speed_y = -self.speed_y
            self.pos_y = height - self.size
        if self.pos_y < self.size:
            self.speed_y = -self.speed_y
            self.pos_y = self.size
        

class ExampleWorld(object):

    def __init__(self, count, width, height):
        self.size_x = width
        self.size_y = height
        self.atoms = []
        self.load_from_xml('atoms.xml')

    def load_from_xml(self, filename):
        root = ET.parse(filename)
        size = root.findall('world')
        # size = size.split(',')
        for i in size:
            # print(i.attrib['sizeX'])
            self.size_x = i.attrib['sizeX']
            self.size_y = i.attrib['sizeY']
        atoms=root.findall('atoms')
        for j in atoms:
            typ = j.find('type')
            typ = j.find('position')
            for k in typ:
                tp=k
            pos = j.text['position']
            color = j.text['color']
            radius = j.text['radius']
            velocity = j.text['velocity']
            if typ == 'Normal':
                self.atoms.append(Atom(pos[0], pos[1], velocity[0], velocity[1], radius, color))
            else:
                self.atoms.append(FallDownAtom(pos[0], pos[1], velocity[0], velocity[1], radius, color))
        for i in self.atoms:
            print(i)
        # print(size)

    def tick(self, size_x, size_y):
        ret = []
        for atom in self.atoms:
            atom.move(size_x, size_y)
            ret.append(atom.to_tuple())
        return tuple(ret)
    
    def get_size(self):
        return (self.size_x, self.size_y)


if __name__ == '__main__':
    size_x, size_y = 400, 300
    world = ExampleWorld(10, size_x, size_y)
    print(world)
    playground.run(world.get_size(), world)

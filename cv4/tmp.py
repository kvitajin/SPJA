class Counter(object):
    count = 0
    no_of_counter = 0

    def __init__(self, count=0):
        self.count = count
        Counter.no_of_counter += 1

    def print_no_of_counters(self):
        print(self.no_of_counter)

    def set_counter(self, count):
        self.count = count

    def get_counter(self):
        return self.count

    def inc_counter(self):
        self.count += 1

    def __add__(self, other):
        cx = Counter()
        cx.set_counter(self.get_counter()+other.get_counter())
        return cx

c1 = Counter()
print(c1.get_counter())
c2 = Counter(5)
print(c2.get_counter())
c1. inc_counter()
c1.print_no_of_counters()
c3 = c1+c2
c3.get_counter()

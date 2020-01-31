class Other(object):

    def implicit(self):
        print("OTHER implicit(). self=", self)

    def override(self):
        print("OTHER override(). self=", self)

    def altered(self):
        print("OTHER altered(). self=", self)


class Child(object):

    def __init__(self):
        self.other = Other()
        print("self=", self, "self.other=", self.other)

    def implicit(self):
        self.other.implicit()
        print("self.other.implicit(). ", "self=", self, "self.other=", self.other)

    def override(self):
        print("CHILD override(). self=", self)

    def altered(self):
        print("CHILD, BEFORE OTHER altered(). self=", self)
        self.other.altered()
        print("CHILD, AFTER OTHER altered(). self=", self)


son = Child()

son.implicit()
son.override()
son.altered()

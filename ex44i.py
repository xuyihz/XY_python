class Parent(object):
    
    def implicit(self):
        print("PARENT implicit(). self=", self)

    def override(self):
        print("PARENT override(). self=", self)

    def altered(self):
        print("PARENT altered(). self=", self)


class Child(Parent):

    def override(self):
        print("CHILD override(). self=", self)

    def altered(self):
        print("CHILD, BEFORE PARENT altered(). self=", self)
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered(). self=", self)


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

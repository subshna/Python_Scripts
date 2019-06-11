class Bird:
    def intro(self):
        print('There are many types of birds')

    def flight(self):
        print('Most of the birds can fly but some cannot')

class sparrow(Bird):
    def flight(self):
        print('Sparrow can fly')

class ostrich(Bird):
    def flight(self):
        print('Ostrich cannot fly')

# Process of re-implementing a method in the child class is know as method Overloading

obj_bird = Bird()
obj_sparrow = sparrow()
obj_ostrich = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_ostrich.intro()
obj_sparrow.flight()

obj_ostrich.intro()
obj_ostrich.flight()
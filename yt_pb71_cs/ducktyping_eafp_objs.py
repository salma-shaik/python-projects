class Duck:
    def quack(self):
        print("Quack Quack")

    def flap(self):
        print("Flap Flap")


class Person:
    def quack(self):
        print("Quacking like a duck")

    def flap(self):
        print("Flapping like a duck")


def quack_and_fly(thing):
    # Not Duck Typed - Unpythonic
    """
    if isinstance(thing, Duck):
        thing.quack()
        thing.flap()
    else:
        print('This has to be a duck')


    thing.quack()
    thing.flap()
 """
    # Asking for permission - Unpythonic. Asking for permission at every stage
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()
    if hasattr(thing, 'flap'):
        if callable(thing.flap):
            thing.flap()

    print()


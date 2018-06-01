import ducktyping_eafp_objs

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

    # LBYL - Asking for permission - Unpythonic. Asking for permission at every stage
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()
    if hasattr(thing, 'flap'):
        if callable(thing.flap):
            thing.flap()
    """

    #Pythonic - EAFP
    try:
        thing.quack()
        thing.flap()
        thing.bark()
    except AttributeError as e:
        print(e)

    print()


duck_obj = ducktyping_eafp_objs.Duck()
quack_and_fly(duck_obj)

pers_obj = ducktyping_eafp_objs.Person()
quack_and_fly(pers_obj)
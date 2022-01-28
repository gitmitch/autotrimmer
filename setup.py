import pygame


def setup():
    print('Now we are going to select which joystick button will activate autotrimmer.')

    number_of_joysticks = joystick_count()

    print(f'You have {number_of_joysticks} joysticks connected.')

def joystick_count():
    pygame.joystick.init()
    return pygame.joystick.get_count()



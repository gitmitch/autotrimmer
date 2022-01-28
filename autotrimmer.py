import setup


print(  """Welcome to Autotrimmer!
This program will set your elevator trim automatically to hold your current pitch.
You activate the Autotrimmer by holding a joystick button. While active, the autotrimmer
will adjust elevator trim to try to keep your aircraft's pitch steady. You hold the joystick
button while relaxing pressure on the yoke, returning it to its neutral position. When you
release the button, your aircraft is perfectly trimmed at pitch you desired with no need
to keep pressure on the yoke.

""")


def main_menu():
    print(  """This is the main menu
Your options are:
> Setup - Pick the joystick button you want to use.
> Connect - Connect to the simulator.
> Disconnect - Disconnect from the simulator.
> Exit - Quit this program.

Enter a command:
    """)

    command = input("> ")

    match(command.lower()):
        case 'setup':
            setup.setup()
        case 'exit':
            print('Thanks for playing!')
            exit()

while True:
    main_menu()
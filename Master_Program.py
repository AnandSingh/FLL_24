from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from TurtleDrive import *
from TurtleAttachement import *
import run_collection, run_boat_shark, run_coral, run_crab, run_krackan
import run_submersible, run_whale, deliver_coral_tree, coral_tree


# Initialize the sensor.
bottom_sensor = ColorSensor(Port.E)  # this is bottom sesor
front_sensor = ColorSensor(Port.F)  # this is front sensor

# Initialize the hub.
hub = PrimeHub()

Color.MY_GREEN = Color(h=155, s=72, v=48)
Color.MY_MAGENTA = Color(h=339, s=79, v=70)
Color.MY_RED = Color(h=352, s=88, v=80)
Color.MY_ORANGE = Color(h=9, s=84, v=99)
Color.MY_BLUE = Color(h=217, s=88, v=69)
Color.MY_BLACK = Color(h=240, s=5, v=24)
Color.MY_YELLOW = Color(h=52, s=71, v=100)
Color.MY_WHITE = Color(h=0, s=0, v=100)
Color.MY_NONE = Color(h=0, s=0, v=0)

colorToDefault = {
    Color.MY_GREEN: Color.GREEN,
    Color.MY_MAGENTA: Color.MAGENTA,
    Color.MY_RED: Color.RED,
    Color.MY_ORANGE: Color.ORANGE,
    Color.MY_BLUE: Color.BLUE,
    Color.MY_BLACK: Color.BLACK,
    Color.MY_WHITE: Color.WHITE,
    Color.MY_NONE: Color.NONE,
}


def scan_colors(sensor):
    # Repeat forever.
    while True:

        # Get the ambient color values. Instead of scanning the color of a surface,
        # this lets you scan the color of light sources like lamps or screens.
        hsv = sensor.hsv(surface=True)
        color = sensor.color(surface=True)

        # Get the ambient light intensity.
        ambient = sensor.ambient()

        # Print the measurements.
        print(str(hsv), str(color), ambient)

        # Point the sensor at a computer screen or colored light. Watch the color.
        # Also, cover the sensor with your hands and watch the ambient value.

        # Wait so we can read the printed line
        wait(500)


def set_colors(sensor):
    # First, decide which objects you want to detect, and measure their HSV values.
    # You can do that with the scan_colors() method.
    #
    # Use your measurements to override the default colors, or add new colors:

    # Put your colors in a list or tuple.
    my_colors = (
        Color.MY_GREEN,
        Color.MY_MAGENTA,
        Color.MY_RED,
        Color.MY_ORANGE,
        Color.MY_BLUE,
        Color.MY_BLACK,
        Color.MY_WHITE,
        Color.MY_NONE,
    )

    # Save your colors.
    sensor.detectable_colors(my_colors)


def show_icon(color):
    if color == Color.MY_GREEN:
        hub.display.icon(Icon.ARROW_RIGHT_DOWN)
        print("Run Green Attanchement")

    if color == Color.MY_MAGENTA:
        hub.display.icon(Icon.ARROW_RIGHT_DOWN)
        print("Run Magenta Attachement")

    if color == Color.MY_WHITE:
        hub.display.icon(Icon.ARROW_RIGHT_DOWN)
        print("Run WHITE Attachment")

    if color == Color.MY_RED:
        hub.display.icon(Icon.ARROW_RIGHT_DOWN)
        print("Run RED Attachement ")

    if color == Color.MY_YELLOW:
        hub.display.icon(Icon.ARROW_RIGHT_DOWN)
        print("Run YELLOW Attachement")

    if color == Color.MY_BLACK:
        hub.display.icon(Icon.ARROW_RIGHT_DOWN)
        print("Run BLACK Attachement")

    if color == Color.MY_ORANGE:
        print("Run ORANGE Attachement ")
        hub.display.icon(Icon.ARROW_RIGHT_DOWN)

    if color == Color.MY_BLUE:
        print("Run BLUE Attachement")
        hub.display.icon(Icon.ARROW_RIGHT_DOWN)

    if color == Color.MY_NONE:
        print("NO Attachement")
        hub.display.icon(Icon.ARROW_UP)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()

    # set the color as we tested
    set_colors(front_sensor)

    # Main loop
    while True:
        while True:
            # SCan the attchment color
            color = front_sensor.color()

            if color == Color.MY_NONE:
                hub.light.off()
            else:
                hub.light.on(colorToDefault[color])

            # Show the arrow
            show_icon(color)

            wait(100)
            # check for the button press
            pressed = hub.buttons.pressed()

            # run the attachment code is button is pressed
            if Button.RIGHT in pressed and color == Color.MY_GREEN:
                print("Run crab")
                run_crab.runBannana_Boat(td)

            if Button.RIGHT in pressed and color == Color.MY_MAGENTA:
                run_collection.run_Krillies(td, ta)
                print("run Krilles")

            if Button.RIGHT in pressed and color == Color.MY_BLUE:
                print("Run whale")
                run_whale.run_whale(td, ta)

            if Button.RIGHT in pressed and color == Color.MY_WHITE:
                print("Run sumersible")
                run_submersible.run_submersible(td, ta)

            if Button.RIGHT in pressed and color == Color.MY_YELLOW:
                print("Run coral")
                run_coral.runCoral(td, ta)

            if Button.RIGHT in pressed and color == Color.MY_RED:
                print("Run deliver coral tree")
                deliver_coral_tree.Deliver_Tree(td, ta)

            if Button.RIGHT in pressed and color == Color.MY_BLACK:
                print("Run kracken")
                run_krackan.run_kracken(td, ta)

            if Button.RIGHT in pressed and color == Color.MY_ORANGE:
                print("Run boat shark")
                run_boat_shark.run_boat_shark(td, ta)


            # run_collection.run_Krillies(td, ta)

            # Implement all other runs, based on the button presses and color

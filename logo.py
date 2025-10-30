from pyfiglet import Figlet
from colors import Colors


def print_logo():
    fig = Figlet(font='slant')
    logo = fig.renderText("iinioi")
    print(Colors.cyan + logo + Colors.reset)
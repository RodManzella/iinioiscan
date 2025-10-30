from pyfiglet import Figlet
from utilities import colors

colors = colors.Colors()

def print_logo():
    fig = Figlet(font='slant')
    logo = fig.renderText("iinioi")
    print(colors.cyan + logo + colors.reset)
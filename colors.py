class Colors:
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    yellow = '\033[93m'
    magenta = '\033[95m'
    cyan = '\033[96m'
    white = '\033[97m'
    reset = '\033[0m'

    @staticmethod
    def colorize(text, color):
        color_code = getattr(Colors, color.lower(), '')
        return f"{color_code}{text}{Colors.reset}"
    
    @staticmethod
    def colorizeResponse(status_code):
        color = 'oi'
        first_number = str(status_code)[0]

        if(first_number == '2'):
            color = 'green'

        elif(first_number == '3'):
            color = 'yellow'

        elif(first_number == '4'):
            color = 'red'

        else:
            color = 'magenta'
        return colorize(str(status_code),color)
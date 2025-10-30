from request_modules.multipleRequests import requestBundle
from utilities.HeaderUtils import HeaderUtils

user_agent = HeaderUtils().get_user_agent()

def readStdinLines(stdin):
    stdInArr = stdin.splitlines()  # split standard input into array (split by newline character)

    for line in stdInArr:
        requestBundle(line, user_agent)

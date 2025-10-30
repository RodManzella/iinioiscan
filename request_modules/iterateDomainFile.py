import os
import sys
from request_modules.multipleRequests import requestBundle
from utilities.HeaderUtils import HeaderUtils


user_agent = HeaderUtils().get_user_agent()

def iterateFile(arg):
    try:
        if(os.path.exists(arg)):
            with open(str(arg), "r") as file:
                for line in file:
                    requestBundle(line, user_agent)
        else:
            showUsage()
    except KeyboardInterrupt:
        print("\n[!] Bye!.")
        sys.exit(0)
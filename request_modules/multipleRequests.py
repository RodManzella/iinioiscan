from request_modules import myRequests
from utilities.HeaderUtils import HeaderUtils
import sys



def makeRequests(url, headers):    
    print(f"Checking: {url}")

    try:
        myRequests.requestOperations(url, headers)
    except KeyboardInterrupt:
        print("\n[!] Bye!.")
        sys.exit(0)

    
    
    print("============================================================\n")


def requestBundle(url, headers): 
    url_tratada = url.strip()
    makeRequests(url_tratada, headers)
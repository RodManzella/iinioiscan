
import requests
from colors import Colors

def requestOperations(url, headers):
    session = requests.Session()
    try:
        reqHttps = session.get("https://" + url, headers=headers, timeout=(1), allow_redirects=False)
        
        print(f"{url}:443 - {colorizeResponse(reqHttps.status_code)} --> {showRedirect(reqHttps)}")
        
    except requests.exceptions.RequestException as e:
        print(f"{url}:443 - ERROR")
        
    try:
        reqHttp = session.get("http://" + url, headers=headers, timeout=(1), allow_redirects=False)
        print(f"{url}:80 - {colorizeResponse(reqHttp.status_code)} --> {showRedirect(reqHttp)}")
        

    except requests.exceptions.RequestException as e:
        print(f"{url}:80 - ERROR")



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
    return Colors.colorize(str(status_code),color)

def showRedirect(request):
    url = ''
    first_number = str(request.status_code)[0]

    if(first_number == '3'):
        url = request.headers.get("Location")
    return url

import requests
from utilities.RedirectionUtils import RedirectionUtils
from utilities.ColorUtils import ColorUtils
from utilities.HeaderUtils import HeaderUtils

user_agent = HeaderUtils().get_user_agent()

printRedirect = RedirectionUtils.showRedirect
colorizeResponse = ColorUtils.colorizeResponse

def requestOperations(url, headers=user_agent):
    session = requests.Session()
    try:
        reqHttps = session.get("https://" + url, headers=headers, timeout=(1), allow_redirects=False)
        
        print(f"{url}:443 - {colorizeResponse(reqHttps.status_code)} --> {printRedirect(reqHttps)}")
        
    except requests.exceptions.RequestException as e:
        print(f"{url}:443 - ERROR")
        
    try:
        reqHttp = session.get("http://" + url, headers=headers, timeout=(1), allow_redirects=False)
        print(f"{url}:80 - {ColorUtils.colorizeResponse(reqHttp.status_code)} --> {printRedirect(reqHttp)}")
        

    except requests.exceptions.RequestException as e:
        print(f"{url}:80 - ERROR")






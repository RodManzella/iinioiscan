class RedirectionUtils:
    

    @staticmethod
    def showRedirect(request):
        url = ''
        first_number = str(request.status_code)[0]

        if(first_number == '3'):
            url = request.headers.get("Location")
        return url
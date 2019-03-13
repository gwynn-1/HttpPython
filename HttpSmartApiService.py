import requests

class HttpSmartApiService:
    "Đối tượng gọi Smart Api"
    # domain = "http://localhost:90/"
    domain = "http://139.59.237.230:8000"

    @staticmethod
    def postApi(api, body, jwt=None):
        try:
            if jwt is None:
                result = requests.post(
                    HttpSmartApiService.domain + api, data=body)
                return result.json()
            else:
                header = {
                    "Authorization": "Bearer "+jwt
                }
                result = requests.post(
                    HttpSmartApiService.domain + api, data=body, headers=header)
                return result.json()
        except requests.exceptions.HTTPError as err:
            print(err)
    @staticmethod
    def getApi(api, jwt=None):
        try:
            if jwt is None:
                result = requests.post(HttpSmartApiService.domain + api)
                return result.json()
            else:
                header = {
                    "Authorization":"Bearer "+jwt
                }
                result = requests.post(HttpSmartApiService.domain + api, headers=header)
                return result.json()
        except requests.exceptions.HTTPError as err:
                print (err)

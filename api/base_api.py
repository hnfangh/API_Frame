import requests

class BaseApi:

    # 二次封装requests方法
    def send(self,data):
        # ** 解包data中json
        return requests.request(**data)

import string
import yaml
from api.base_api import BaseApi


class GetToken(BaseApi):

    _corpid = "wwe2b87cba46fecb13"
    _corpsecret = "zXw69_DpO8A77XI6hgDKFV58So0eXdiLPhJL3KwLrOk"

    # 模版替换Yaml文件的变量值
    def template(self):
        with open("../api/token.yaml", "r") as f:
            st = string.Template(f.read()).substitute(corpid=self._corpid,
                                                      corpsecret=self._corpsecret)
            return yaml.safe_load(st)

    # 获取token
    def getToken(self):
        # 在传递yaml之前，进行yaml的模版替换，之后调用template方法
        data = self.template()
        res = self.send(data)
        token = res.json()['access_token']
        return token


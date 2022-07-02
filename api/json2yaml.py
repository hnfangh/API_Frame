import yaml

class TestsJson2Yaml:

    # 封装json数据格式转为yaml数据格式
    def test_json_to_yaml(self):

        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": 1,
                "corpsecret": 2
            }
        }

        with open("token.yaml", "w") as f:
            yaml.safe_dump(data,f)


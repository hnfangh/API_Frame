
# 企业微信API_Automation

## APIObject

    - api 基础API目录
        base_api.py 封装基础request封装，**data传参以字典形式解包
        get_token.py 封装通用token的获取
        joson2yaml.py json参数转为yaml文件，进行数据的驱动
        assert.py 封装通用断言方式 statecode\data\text
        db_model.py 封装通用的数据库操作

    - report 报告生成目录

    - utils 工具类
        log_util.py 封装日志打印

        
    - testcase 测试用例的目录
        test_address.py 测试具体的业务方法并断言

通过yaml文件数据驱动
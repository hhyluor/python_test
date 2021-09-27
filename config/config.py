import yaml
import os
class configModel:
    def __init__(self, url, DB_NAME = '', Charset = ''):
        currPath=os.path.dirname(os.path.realpath(__file__))
        f = open(currPath+url)
        # yaml.warnings({'YAMLLoadWarning': False})
        conf = yaml.load(f, Loader=yaml.FullLoader)

        # logging.info(conf)
        # DC 数据库连接，DC_DB_NAME根据情况修改
        self.DC_DB_URL = conf["DataCenter"]["DC_DB_URL"]
        self.DC_DB_USER = conf["DataCenter"]["DC_DB_USER"]
        self.DC_DB_PASS = conf["DataCenter"]["DC_DB_PASS"]
        self.DC_DB_PORT = conf["DataCenter"]["DC_DB_PORT"]
        self.DB_NAME = DB_NAME

        if Charset:
            self.Charset = Charset
        else:
            self.Charset = 'utf8'

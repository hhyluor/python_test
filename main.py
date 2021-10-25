import logging
import os
import sys
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from config.config import configModel
from service import test
import decimal
import datetime
import numpy as np

# logging.basicConfig函数对日志的输出格式及方式做相关配置
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

try:
    env = sys.argv[2]
except :
    env = 'sit'


class JSONEncoder(_JSONEncoder):
    def default(self, o):

        if isinstance(o, decimal.Decimal):
            return float(o)

        elif isinstance(o, np.integer):
            return int(o)

        elif isinstance(o, datetime.date):
            return o.strftime('%Y-%m-%d')

        super(JSONEncoder, self).default(o)


class Flask(_Flask):
    json_encoder = JSONEncoder


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/test', methods=['POST'])
def cal_test1():
    data = test.test1()
    logging.info('111111')
    logging.info('222222')
    logging.info('333333')
    logging.info('444444')
    logging.info('555555')
    logging.info('666666')
    logging.info('777777')
    return data


@app.route('/test1', methods=['POST'])
def cal_test():
    data = test.test1()
    logging.info('111111')
    logging.info('222222')
    logging.info('333333')
    logging.info('444444')
    logging.info('555555')
    logging.info('666666')
    logging.info('777777')
    return data


if __name__ == '__main__':
    # 服务器模式
    try:
        app.run(host='0.0.0.0', debug=False, port=sys.argv[1])
    except:
        app.run(host='0.0.0.0', debug=False, port=9999)

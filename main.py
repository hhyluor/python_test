import os
import sys
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from config.config import configModel
from service import test
import decimal
import datetime
import numpy as np


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
def cal_test():
    data = test.test1()

    return data


if __name__ == '__main__':
    # 服务器模式
    try:
        app.run(host='0.0.0.0', debug=False, port=sys.argv[1])
    except:
        app.run(host='106.14.34.215', debug=False, port=9999)

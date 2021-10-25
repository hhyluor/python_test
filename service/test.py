import json
import logging


def test1():
    logging.info('------111111-------')
    logging.info('------222222-------')
    logging.info('------333333-------')
    logging.info('------444444-------')
    logging.info('------555555-------')
    logging.info('------666666-------')
    logging.info('------777777-------')
    return json.dumps({"message": "OK"})

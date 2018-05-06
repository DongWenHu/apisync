# -*- coding: utf-8 -*-

import logging
import os
from apisync.settings import BASE_DIR

LOG_FORMAT = '\n'.join((
    '/' + '-' * 80,
    '[%(levelname)s][%(asctime)s][%(process)d:%(thread)d][%(filename)s:%(lineno)d %(funcName)s]:',
    '%(message)s',
    '-' * 80 + '/',
))

logger = logging.getLogger('apisync')
handler = logging.FileHandler(os.path.join(BASE_DIR, "logs/apisync.log"))
handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

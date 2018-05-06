#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools
import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_MISSED
import config
from share.apis.afftrack import AfftrackApi
from share.apis.yeahmobi import YeahMobiApi
from share.log import logger

sched = BackgroundScheduler()


def log_call(func):
    @functools.wraps(func)
    def func_wrapper(*args, **kwargs):
        # logger.debug('func: %s', func.__name__)
        return func(*args, **kwargs)

    return func_wrapper


def error_listener(event):
    if event.exception:
        logger.fatal('job %s error. scheduled_run_time: %s, exception: %s, traceback:\n%s',
                     event.job_id, event.scheduled_run_time, event.exception, event.traceback)
    else:
        logger.info('job %s miss', event.job_id)


@sched.scheduled_job('interval', seconds=config.API_SYNC_INTERVAL_SECONDS)
def api_sync():
    # 每隔1个小时同步一次
    # offers = YeahMobiApi.get_all_offers()
    # AfftrackApi.create_offer()
    # AfftrackApi.update_offer()
    pass


def run():
    sched.add_listener(error_listener, EVENT_JOB_ERROR | EVENT_JOB_MISSED)
    sched.start()

    while 1:
        try:
            time.sleep(1)
        except:
            break

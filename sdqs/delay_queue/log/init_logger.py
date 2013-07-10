import logging
import logging.handlers


def initLogger(path, size, count):
    try:
        log = logging.getLogger('delay_queue')
        handler = logging.handlers.RotatingFileHandler(filename=path, maxBytes=size, backupCount=count)
        formatter= logging.Formatter('[%(asctime)s] %(name)s [%(filename)s, %(lineno)d] [%(levelname)s] %(message)s')
        handler.setFormatter(formatter)

        log.addHandler(handler)
        log.setLevel(logging.INFO)
        return log
    except Exception:
        print 'initLogger unexpected exception'
        return None



DQ_LOGGER = initLogger("/var/log/delay_queue/dq.log", 4096*1024, 5)
DQ_LOGGER.setLevel(logging.DEBUG)


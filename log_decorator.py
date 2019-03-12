import logging
import traceback
from logging.handlers import TimedRotatingFileHandler

def loggerInFile(filename):
    def trace_func(func):
        def tmp(*args, **kwargs):
            # 日志路径
            log_filepath = filename
            # 实例化logging
            logger = logging.getLogger()
            # 配置日志级别
            logger.setLevel(logging.INFO)
            # when:滚动的时间； interval：是指等待多少个单位when的时间后，Logger会自动重建文件；
            # backupCount：是保留日志个数。默认的0是不会自动删除掉日志
            handler = TimedRotatingFileHandler(log_filepath, when='MIDNIGHT', interval=1, backupCount=5)
            # 配置日志打印信息  %(asctime)s:打印日志时间  %(levelname)s：打印日志级别名称  %(message)s:打印日志信息
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            try:
                logger.info(func.__name__)
                result = func(*args, **kwargs)
                logger.info('%s'%result)
            except:
                logger.error(traceback.format_exc())
        return tmp
    return trace_func

@loggerInFile('./newlog.log')
def test(n):

    return 100/n
    # print(test.__name__)

test(2)
print(test.__name__)


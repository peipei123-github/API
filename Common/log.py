import logging

def log():
    #使用basicconfig方法设置格式
    logging.basicConfig(level=logging.INFO,
                        format='日志：%(name)s-级别：%(levelname)s-模块：%(module)s.py-时间：%(asctime)s-第%(lineno)s行：%(message)s')
    #定义一个日志记录器
    logger=logging.getLogger('api框架第二遍')
    #返回给外界
    return logger

#单例模式
logger=log()

if __name__ == '__main__':
    logger.info('test')
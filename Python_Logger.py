import logging

# Create and Configure Logger
LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename='E:\Subash\Python_Scripts\RobotFramework\lumberjack.log',
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()

# Test Messages
logger.debug('This is a debug message')
logger.info('Info message of the log')
logger.warning('Warning has been issued')
logger.error('Divided by zero')
logger.critical('The device is down')
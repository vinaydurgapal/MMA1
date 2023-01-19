# import logging
# import os
#
# class LogGen():
#     @staticmethod
#     def loggen():
#         # os.path.abspath(os.curdir) +
#        # path = os.path.abspath(os.curdir) + '//logs//automation.log'
#         fileHandler = logging.FileHandler('logfile.log')
#         # logging.basicConfig(filename=path,
#         #                     format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger = logging.getLogger()
#         logger.setLevel(logging.DEBUG)
#         return logger


import logging
class LogGen():
  def loggen():
# getLogger() method takes the test case name as input
    logger = logging.getLogger(__name__)
# FileHandler() method takes location and path of log file
    fileHandler = logging.FileHandler('C:/Users/Cliffex/PycharmProjects/MMA1/logs/automations.log')
# Formatter() method takes care of the log file formatting
    formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
# addHandler() method takes fileHandler object as parameter
    logger.addHandler(fileHandler)
# setting the logger level
    logger.setLevel(logging.WARN)
    return logger

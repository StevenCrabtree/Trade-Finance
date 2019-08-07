'''
Created on Aug 7, 2019

@author: Brian

Initialization function
Read configuration
Open loging file
Open result file
'''
import os
import datetime as dt
import time
import configparser
import logging

'''
Logging controls
'''
LOGGING_LEVEL = logging.DEBUG
LOGGING_FORMAT = '%(asctime)s: %(levelname)s: %(message)s'

def initialize():
    now = dt.datetime.now()
    
    config_file = os.getenv('localappdata') + "\\Development\\tradefinance.ini"
    config = configparser.ConfigParser()
    config.read(config_file)
    config.sections()
    ini_data = config['TRADEFINANCE']
    tf_dir = ini_data['dir']
    tf_data = ini_data['data']
    tf_log = tf_dir + "\\" + ini_data['log']
    tf_result = tf_dir + "\\" + ini_data['result']

    logging.basicConfig(filename=tf_log, level=LOGGING_LEVEL, format=LOGGING_FORMAT)
    print ("Logging to", tf_log)
    logger = logging.getLogger('trade_finance_logger')
    log_fmt = logging.Formatter('%(asctime)s - %(name)s - %levelname - %(messages)s')
    logger.info('Logging initialized for Trade Financing analysis')
    
    output_file = tf_result + ' {:4d} {:0>2d} {:0>2d} {:0>2d} {:0>2d} {:0>2d}'.format(now.year, now.month, now.day, \
                                                                                              now.hour, now.minute, now.second) + '.txt'
    f_out = open(output_file, 'w')

    return (f_out)
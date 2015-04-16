# -*- coding: utf-8 -*- 

import com_appConst
import glob
import logging
import logging.handlers
from datetime import datetime as dt

LOG_FILENAME = '/tmp/agri_post4.log'

#com_func
class loggingClass:

    def __init__(self):
        print ""
        
    def debug(self, sStr):
    	tdatetime = dt.now()
    	sDate = tdatetime.strftime('%Y/%m/%d %H:%M:%S')
    	
    	my_logger = logging.getLogger('MyLogger')
    	my_logger.setLevel(logging.DEBUG)
    	nByte = 1024 * 50
    	handler = logging.handlers.RotatingFileHandler( LOG_FILENAME, maxBytes=nByte, backupCount=3 )
    	my_logger.addHandler(handler)
    	my_logger.debug(sDate +" "+ sStr);
    	
    def test(self, sStr):
    	tdatetime = dt.now()
    	sDate = tdatetime.strftime('%Y/%m/%d %H:%M:%S')
    	
    	my_logger = logging.getLogger('MyLogger')
    	my_logger.setLevel(logging.DEBUG)
    	nByte = 1024 * 50
    	handler = logging.handlers.RotatingFileHandler( LOG_FILENAME, maxBytes=nByte, backupCount=3 )
    	my_logger.addHandler(handler)
    	#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        #ch = logging.StreamHandler()
        #ch.setLevel(logging.DEBUG)
        #ch.setFormatter(formatter)
        #my_logger.addHandler(ch)
    	my_logger.debug(sDate +" "+ sStr);


#    	log_fmt = '%(asctime)s- %(levelname)s - %(message)s'
#   	logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,format=log_fmt)
#    	logging.debug( sStr)

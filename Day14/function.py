# Author:Jack
# Date:2018/8/19

# subroutine procedure

import time
time_format = '%Y-%m-%d %X'
time_current = time.strftime(time_format)

def logger(n):
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('log','a') as log:
        log.write('%s %s\n'%(time_current,n))

logger(1)
logger(2)

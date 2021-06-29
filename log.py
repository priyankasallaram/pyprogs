# Write your code here :-)
import logging
logging.basicConfig(level=logging.INFO, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of Program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' %(n))
    total = 1
    for i in range(1,n+1):
        total*=i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
        logging.debug('End of factorial(%s%%)'  % (n))
        logging.info('The info logging module is working.')
        logging.warning('An error message is about to be logged.')
        logging.error('An error has occurred.')
        logging.critical('The program is unable to recover!')
    return total

_n = input()
factorial(int(_n))

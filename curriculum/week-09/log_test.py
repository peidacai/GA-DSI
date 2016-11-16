import logging



logging.basicConfig(filename = 'log_test.log', filemode='w', level = logging.DEBUG)
log = logging.getLogger(__name__)

#log.critical("Not an integer")

def factorial(n):
	log.info('Just running the function')
	if type(n) == type(1):
		if n > 1:
			return (factorial(n-1))*n
		else:
			return 1
	else:
		log.critical('Needs an integer!')



fact_list = [1,2,3,'str']
for i in fact_list:
	print factorial(i)
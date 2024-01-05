import logging

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
#logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w', format='%(levelname)s - %(message)s')
logging.info('aaa')

logger=logging.getLogger(__name__)

handler=logging.FileHandler(filename='test.log',mode='a')

formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(name)s')

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info('Accc')
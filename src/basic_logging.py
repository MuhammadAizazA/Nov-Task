import logging
def check_package_working():
    print("Package is working")
    
if __name__=='__main__':
    check_package_working()
 
    logging.basicConfig(filename='app.log',filemode='a',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
    logging.debug("After: Hi this is debuging test")
    logging.warning("After: This is just a warning!")
    logging.info('Admin logged in')
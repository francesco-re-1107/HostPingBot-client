import logging

def to_int(value):
    try:
        return int(value)
    except:
        return None
    
def get_logger():

    LOGGER = logging.getLogger("hostpingbot-client")
    LOGGER.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
    LOGGER.addHandler(ch)

    return LOGGER
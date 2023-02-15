import requests
import time
import os
import logging

BASE_URL = "https://hostpingbot.francescore.dev/update/"
TOKEN = os.environ.get("TOKEN")
TIMEOUT = os.environ.get("TIMEOUT", 10)
INTERVAL = os.environ.get("INTERVAL", 60)
RETRY_AFTER = os.environ.get("RETRY_AFTER", 10)

# Setup logger
LOGGER = logging.getLogger("hostpingbot-client")
LOGGER.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
LOGGER.addHandler(ch)


def main():
    if TOKEN is None:
        LOGGER.exception("TOKEN environment variable not set")
        raise Exception("TOKEN environment variable not set")

    LOGGER.info("Starting hearbeat with the following parameters:")
    LOGGER.info(f"TOKEN: {TOKEN} seconds")
    LOGGER.info(f"TIMEOUT: {TIMEOUT} seconds")
    LOGGER.info(f"INTERVAL: {INTERVAL} seconds")
    LOGGER.info(f"RETRY_AFTER: {RETRY_AFTER} seconds")

    while True:
        try:
            requests.post(BASE_URL + TOKEN, timeout=TIMEOUT)
            LOGGER.info(f"Heartbeat sent, waiting for {INTERVAL} seconds")
            time.sleep(INTERVAL)
        except:
            LOGGER.warning(f"Cannot send heartbeat, retrying in {RETRY_AFTER} seconds")
            time.sleep(RETRY_AFTER)

if __name__ == "__main__":
    main()
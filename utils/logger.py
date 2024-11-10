import logging

def setup_logger():
    logging.basicConfig(filename='training.log', level=logging.INFO)
    logging.info("Training started")

def log_action(action):
    logging.info(f"Action taken: {action}")

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  #to create a log of the time when the functions were created or smthng like tht

#where to save my logs?

log_path = os.path.join(os.getcwd(),"logs") # get cwd means get current working directory

os.makedirs(log_path,exist_ok=True)

LOG_FILEPATH = os.path.join(log_path,LOG_FILE)  #in the "logs" folder we will create a ".log" file

logging.basicConfig(level = logging.INFO,  #there r diff levels of logging doc  see "python logger"   til INFO level and above it captures all the info
        filename = LOG_FILEPATH,
        format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s" #asctime:current time, lineno: line no at which line we need
        # to log the info then name then label name and message
)

#to test the logger file we created "test.py"


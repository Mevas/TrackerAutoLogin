import logging
import os
import sys

from selenium.webdriver.remote.remote_connection import LOGGER as seleniumConnectionLogger
from selenium.webdriver.common.selenium_manager import logger as seleniumManagerLogger
from selenium.webdriver.common.service import logger as seleniuServiceLogger
from urllib3.connectionpool import log as urllibLogger

from init_configs import read_valid_json_file

# Set the threshold for selenium
seleniumConnectionLogger.setLevel(logging.INFO)
seleniumManagerLogger.setLevel(logging.INFO)
seleniuServiceLogger.setLevel(logging.INFO)
# Set the threshold for urllib3
urllibLogger.setLevel(logging.WARNING)
dir_ = os.path.join(os.getcwd(), "config/logs/")
if os.path.isdir(dir_) == False:
    os.makedirs(dir_)

log_filename = os.path.join(dir_, "trackerautologin.log")

user_config = read_valid_json_file(
    os.path.join(os.getcwd(), "config/user_config.json"), "r"
)

assert user_config["LogLevel"].lower() in [
    "debug",
    "info",
    "error",
    "warning",
], "LogLevel must be ['debug', 'info', 'warning', 'error']"

assert user_config["LogType"].lower() in [
    "file",
    "stderr",
], "'LogType' must be ['file', 'stderr']"

if user_config["LogType"].lower() != "file":
    if user_config["LogLevel"].lower() == "debug":
        logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    if user_config["LogLevel"].lower() == "info":
        logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    elif user_config["LogLevel"].lower() == "warning":
        logging.basicConfig(level=logging.WARNING, stream=sys.stdout)
    else:
        logging.basicConfig(logging=logging.ERROR, stream=sys.stdout)
else:
    if user_config["LogLevel"].lower() == "debug":
        logging.basicConfig(filename=log_filename, level=logging.DEBUG)
    if user_config["LogLevel"].lower() == "info":
        logging.basicConfig(filename=log_filename, level=logging.DEBUG)
    elif user_config["LogLevel"].lower() == "warning":
        logging.basicConfig(filename=log_filename, level=logging.WARNING)
    else:
        logging.basicConfig(filename=log_filename, level=logging.ERROR)

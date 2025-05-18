# --------------------------------------------------
# -- Advanced_Lessons => Add Logging To Your Code --
# --------------------------------------------------
# - Print Out To Console Or File
# - Print Logs Of What Happens
# ------------------------------
# Types Of Logging
# - DEBUG
# - INFO
# - WARNING
# - ERROR
# - CRITICAL
# ----------
# name => Logging Module Give It To The Default Logger.
# -----------------------------------------------------
# Basic Config
# - level => Level of Severity 
# - filename => File Name and Extension of the Log File
# - mode => Mode Of The File a => Append so it will add the new logs
# # to the end of the file or w => Write so it will overwrite the file 
# - format => Format For The Log Message to be more readable
# - datefmt => Date Format to be more readable
# ------------------------
# getLogger => Return a Logger With the Specified Name default is root

import logging

# print(dir(logging))

# By default, log files are created in the current working directory
# You can specify an absolute path if needed like: "C:/logs/my_app.log" or "/var/log/my_app.log"
logging.basicConfig(filename="C:/new/python/learning/Advanced Topics/my_app.log", # the logging file name
                    filemode="a",
                    format="(%(asctime)s) | %(name)s | %(levelname)s => '%(message)s'",
                    datefmt="%d - %B - %Y, %H:%M:%S")
# format asctime => Date and Time at the start of the log message
# name => Name of the logger
# levelname => Level of the log message ( DEBUG, INFO, WARNING,
#  ERROR, CRITICAL)

my_logger = logging.getLogger("Elzero") # Get The Logger With The Name Elzero
# instead of using the default logger root

my_logger.warning("This Is Warning Message") # Log A Warning Message
my_logger.error("This Is Error Message") # Log An Error Message
my_logger.critical("This Is Critical Message") # Log A Critical Message
my_logger.info("This Is Info Message") # Log An Info Message
my_logger.debug("This Is Debug Message") # Log A Debug Message
# here the log file will be created in the same directory as the python file
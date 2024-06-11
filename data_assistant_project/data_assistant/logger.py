from datetime import datetime
import os

class Logger:
    def __init__(self, log_file=None):
        self.log_file = log_file

    def set_log_file(self, log_file):
        self.log_file = log_file

    def log(self, message):
        if self.log_file:
            with open(self.log_file, "a") as log:
                log.write(f"{datetime.now()}: {message}\n")
        else:
            print(f"Log file not set: {message}")

    def log_error(self, error_message):
        self.log(f"ERROR: {error_message}")

import time
import threading
import os

class classlog():

    def __init__(self, className : str, debug = False ):
        '''
        This class is used for logging.

        Args:
            className (str): The name of the class that is logging .
            
        '''

        self.className = className
        self.debug = debug

        # Create log folder if not exist
        # Always create log folder in the same directory as this file
        self.rootPath = f"{os.path.abspath(__file__)}/../logFile"
        if not os.path.exists(self.rootPath):
            os.makedirs(self.rootPath)

        # Create log file
        self.currentDate = time.strftime("%Y-%m-%d", time.localtime())
        self.logFilePath = f"{self.rootPath}/{self.currentDate}-{self.className}.log"
        self.logFile = open(self.logFilePath, 'a', encoding="utf-8")
        self.fileState = True
        self.log("====================================================================")
        self.log("NEW INSTANCE RUNNING")

        # Start thread for checking date
        self.thread = threading.Thread(target=self.run)
        self.thread.start()
        
        # Enable debug mode
        if(self.debug):
            self.log = self.log_debug
        
    def run(self):
        while True:
            # Create new log file every day
            if(self.currentDate != time.strftime("%Y-%m-%d", time.localtime())):
                self.fileState = False
                self.currentDate = time.strftime("%Y-%m-%d", time.localtime())
                self.logFile.close()
                self.logFilePath = f"{self.rootPath}/{self.currentDate}-{self.className}log.log"
                self.logFile = open(self.logFilePath, 'a', encoding="utf-8")
                self.fileState = True
            else :
                time.sleep(60)
                self.logFile.flush()
            
    def log(self, msg : str):
        '''
        To log your message in the format of [YYYY-MM-DD HH:MM:SS] msg
        '''

        logMsg = time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()) + " " + msg +"\n"
        if(self.fileState):
            self.logFile.write(logMsg)
        else :
            while not self.fileState:
                time.sleep(1)
            self.logFile.write(logMsg)

    def log_debug(self, msg : str):
        '''
        To log your message in the format of [YYYY-MM-DD HH:MM:SS] msg
        Debug mode will flush the log file after every log
        '''

        logMsg = time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()) + " " + msg +"\n"
        if(self.fileState):
            self.logFile.write(logMsg)
            self.logFile.flush()
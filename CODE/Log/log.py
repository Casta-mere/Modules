import time
import threading
    
class classlog():

    def __init__(self,className):
        self.currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.currentDate = time.strftime("%Y-%m-%d", time.localtime())
        self.className = className
        self.LogPath = f"{self.currentDate}-{self.className}log.log"
        self.logFile = open(self.LogPath, 'a', encoding="utf-8")
        self.fileState = True
        self.log("====================================================================")
        self.log("NEW INSTANCE RUNNING")

        # Start thread for checking date
        self.thread = threading.Thread(target=self.run)
        self.thread.start()
    
    def run(self):
        while True:
            # Create new log file every day
            if(self.currentDate != time.strftime("%Y-%m-%d", time.localtime())):
                self.fileState = False
                self.currentDate = time.strftime("%Y-%m-%d", time.localtime())
                self.logFile.close()
                self.LogPath = f"{self.currentDate}-{self.className}log.log"
                self.logFile = open(self.LogPath, 'a', encoding="utf-8")
                self.fileState = True

    def log(self,msg):
        if(self.fileState):
            self.logFile.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + msg +"\n")
            self.logFile.flush()
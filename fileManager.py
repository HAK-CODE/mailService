import os
from datetime import datetime as dt


class FileManager:
    fileName = None

    def setFile(self, fileName):
        self.fileName = fileName
        if not os.path.isfile(self.fileName):
            f = open(self.fileName, 'w+')
            f.writelines(str(dt.now()) + '\n')
            f.writelines(str(dt.now()) + '\n')
            f.writelines(str(dt.now()))
            f.close()

    def addLine(self, time, lineNo=0):
        with open(self.fileName, 'r') as file:
            data = file.readlines()
        data[lineNo] = time + '\n'
        with open(self.fileName, 'w') as file:
            file.writelines(data)
        file.close()

    def getDirTime(self):
        with open(self.fileName, 'r') as file:
            data = file.readlines()
        file.close()
        dateObj = dt.strptime(data[0].rstrip(), '%a %b %d %H:%M:%S %Y')
        return dateObj

    def getEmailTime(self, screen=False):
        with open(self.fileName, 'r') as file:
            data = file.readlines()
        file.close()
        dateObj = dt.strptime(data[1 if screen else 2].rstrip(), '%a %b %d %H:%M:%S %Y')
        return dateObj
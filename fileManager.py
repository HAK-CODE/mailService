import os


class FileManager:
    fileName = None
    fileObj = None

    def setFile(self, fileName):
        self.fileName = fileName
        if not os.path.isfile(self.fileName):
            open(self.fileName, 'w+')

    def addLine(self, time, dir=bool):
        file = open(self.fileName, 'a')
        file.write(time+'\n')
        file.close()
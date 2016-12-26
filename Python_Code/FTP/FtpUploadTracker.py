# -*- coding:utf-8 -*-
# file: pyftp.py
#
class FtpUploadTracker:
    sizeWritten = 0
    totalSize = 0
    lastShownPercent = 0

    def __init__(self, totalSize):
        self.totalSize = totalSize

    def handle(self, block):
        self.sizeWritten += 1024
        # percentComplete = round((self.sizeWritten / self.totalSize) * 100)
        percentComplete = round((float(self.sizeWritten) / float(self.totalSize)) * 100)

        if (self.lastShownPercent != percentComplete):
            self.lastShownPercent = percentComplete
            print(str(percentComplete) + " percent complete")

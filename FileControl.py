import os
import csv
class FileControl(object):
    def __init__(self,dictionary,tablename,mode,columns=[]):
        self.writer=self.createWriter(dictionary,tablename,mode,columns=[])

    def write2Table(self, data=[]):
        self.writer.writerow(data)


    def createWriter(self,dictionary,tablename,mode,columns=[]):
        filename='{0}/{1}.csv'.format(dictionary,tablename)
        f=open(filename,mode,encoding="utf-8")
        writer = csv.writer(f)
        if mode=="w" and len(columns)>0:
            writer.writerow(columns)
            return writer
        elif mode=="a" and len(columns)==0:
            return writer


from time import strftime

def get_timestamp():
    return strftime("%Y-%m-%d %H:%M:%S")

class log_status:
    def __init__(self,logpath):
        self.logpath=logpath

    def logsav(self,msg):
        print(msg)
        with open(self.logpath, 'a') as fout:
            fout.write('time:{0}......{1}\n'.format(get_timestamp(), msg))

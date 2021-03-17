import datetime

class Logkeeper():

    def lgwrite(self,message):
        try:
            ct = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = ct + " " + message + "\n"
            logfile = open("log.txt","a+")
            logfile.write(message)
            logfile.close()
        except:
            print("Failed to write log")


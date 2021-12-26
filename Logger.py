from datetime import datetime
import logging

class App_Logger:
    def __init__(self,file_object):
        self.file_object=file_object


    def log(self, log_message):
        # now=datetime.now()
        # date=now.date()
        # current_time=now.strftime("%H:%M:%S")
        # # file_object = open("Logs/Auto_Review_Xpath.txt"+datetime.now().strftime("%d_%m_%Y-%I_%M_%S_%p"), 'a+')
        # self.file_object.write(
        #     str(date) + "/" + str(current_time) + "\t\t" + log_message + "\n")
        try:
            logging.basicConfig(filename=self.file_object, filemode='a', format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
            logging.info(log_message)
        except Exception as e:
            logging.info("Error occured while writing the logs {0}".format(str(e)))





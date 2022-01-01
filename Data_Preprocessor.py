import pandas as pd
from datetime import datetime
from Logger import App_Logger
from Operations import back_Operations

class Data_preprocessor():
    def __init__(self):
        self.xpath=[]
        self.round_brackets_check=[]
        self.square_brackets_check=[]
        self.single_quotes_check=[]
        self.double_quotes_check=[]
        self.asterisk_presence=[]
        self.single_slash_start=[]
        self.only_integers=[]
        self.slashes_absence=[]
        self.square_brackets_presence=[]
        self.file_object="Logs/Data_Preprocessing-"+datetime.now().strftime("%d_%m_%Y-%I_%M_%S_%p")+".log"
        self.logger=App_Logger(file_object=self.file_object)
        self.bo=back_Operations()





    def create_empty_dataframe(self):
        try:
            self.logger.log(log_message="Creating an empty dataframe as part of data preprocessor")

            dataframe=pd.DataFrame()

            return dataframe

        except Exception as e:
            self.logger.log(log_message="Error occured while creating an empty dataframe as part of data preprocessor {0}".format(str(e)))


    def create_round_brackets_list(self,Testable_Property):
        try:
            self.logger.log(log_message="Appending to the round brackets list")

            round_brackets=self.bo.round_Brackets_Check(Testable_property=Testable_Property)
            if round_brackets is True:
                flag='Yes'
            else:
                flag='No'
            self.round_brackets_check.append(flag)

        except Exception as e:
            self.logger.log(log_message="Error occured while appending to the round brackets list {0}".format(str(e)))

    def create_square_brackets_list(self, Testable_Property):
        try:
            self.logger.log(log_message="Appending to the squared brackets list")

            square_brackets = self.bo.square_Brackets_Check(Testable_property=Testable_Property)
            if square_brackets is True:
                flag = 'Yes'
            else:
                flag = 'No'
            self.square_brackets_check.append(flag)

        except Exception as e:
            self.logger.log(log_message="Error occured while appending to the square brackets list {0}".format(str(e)))

    def create_single_quotes_list(self, Testable_Property):
        try:
            self.logger.log(log_message="Appending to the single quotes list")

            single_quotes = self.bo.single_Quotes_Check(Testable_property=Testable_Property)
            if single_quotes is True:
                flag = 'Yes'
            else:
                flag = 'No'
            self.single_quotes_check.append(flag)

        except Exception as e:
            self.logger.log(log_message="Error occured while appending to the single quotes list {0}".format(str(e)))


    def create_double_quotes_list(self, Testable_Property):
        try:
            self.logger.log(log_message="Appending to the double quotes list")

            double_quotes = self.bo.double_Quotes_Check(Testable_property=Testable_Property)
            if double_quotes is True:
                flag = 'Yes'
            else:
                flag = 'No'
            self.double_quotes_check.append(flag)

        except Exception as e:
            self.logger.log(log_message="Error occured while appending to the double quotes list {0}".format(str(e)))

    def create_asterisk_presence_list(self,Testable_Property):
        try:
            self.logger.log(log_message="Appending to the asterisk presence list")

            asterisk_check=self.bo.asterisk_Check(Testable_property=Testable_Property)
            if asterisk_check is True:
                flag = 'Yes'
            else:
                flag = 'No'
            self.asterisk_presence.append(flag)

        except Exception as e:
            self.logger.log(log_message="Error occured while appending to the asterisk presence list {0}".format(str(e)))

    def create_single_slash_start_list(self, Testable_Property):
        try:
            self.logger.log(log_message="Appending to the single slash start list")

            single_slash_start_check = self.bo.single_Slash_Start_Check(Testable_property=Testable_Property)
            if single_slash_start_check is True:
                flag = 'Yes'
            else:
                flag = 'No'
            self.single_slash_start.append(flag)

        except Exception as e:
            self.logger.log(
                log_message="Error occured while appending to the single slash start list {0}".format(str(e)))

    def create_slashes_absence_check_list(self,Testable_Property):
            try:
                self.logger.log(log_message="Appending to slashes absence check list")

                slashes_absence_check = self.bo.slas(Testable_property=Testable_Property)
                if single_slash_start_check is True:
                    flag = 'Yes'
                else:
                    flag = 'No'
                self.single_slash_start.append(flag)

            except Exception as e:
                self.logger.log(
                    log_message="Error occured while appending to the slashes absence start list {0}".format(str(e)))

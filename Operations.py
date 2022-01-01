import pandas as pd
import re
import os
from datetime import datetime
from Custom_Exceptions import EmptyFileException
from werkzeug.utils import secure_filename
from Logger import App_Logger

#logger=Logger.App_Logger()


class back_Operations():
    def __init__(self):

        # self.file_object=open("Logs/Auto_Review_Xpath-"+datetime.now().strftime("%d_%m_%Y-%I_%M_%S_%p")+".log",'a')
        self.file_object="Logs/Auto_Review_Xpath-"+datetime.now().strftime("%d_%m_%Y-%I_%M_%S_%p")+".log"
        self.logger=App_Logger(file_object=self.file_object)



    def file_Reader(self,filename):
        """ This method just reads the input file from the location"""
        try:
            self.logger.log(log_message="Reading the file {0} entered by user".format(filename))
            fname = filename
            dataframe=pd.read_excel(fname,sheet_name='Object repository')
            return dataframe
        except Exception as e:
            print('Exception occured while reading the file \t',str(e))
            self.logger.log(log_message="Exception occured while reading the file {0}\t".format(str(e)))

    def check_File_empty(self,dataframe):
        try:
            self.logger.log(log_message="Checking if file is empty")
            is_empty=dataframe.empty
            if is_empty:
                raise EmptyFileException()
                self.logger.log(log_message=EmptyFileException)
            else:
                return dataframe
        except Exception as e:
            print('Exception occured while checking if the file is empty - \t', str(e))
            self.logger.log(log_message="Exception occured while checking if the file is empty - \t{0}".format(str(e)))

    def create_Review_Columns(self,dataframe):
        """ This method adds the review column in the existing dataframe"""
        try:
            self.logger.log(log_message="Creating the Review columns")
            review_column_name='Auto Code Review'
            review_suggestion='Review Suggestions'
            dataframe[review_column_name]=''
            dataframe[review_suggestion]=''
            updated_dataframe=dataframe
            return updated_dataframe,review_column_name,review_suggestion
        except Exception as e:
            print('Exception occured while creating the review columns \t', str(e))
            self.logger.log(log_message="Exception occured while creating the review columns\t {0}".format(str(e)))


    def select_Column_For_Test(self,dataframe,column_name):
        try:
            self.logger.log(log_message="Selecting column from input file to perform review")
            if column_name in dataframe.columns:
               Testable_Column= dataframe[column_name]
               return Testable_Column

            else:
                return "Column is not present in file"
                self.logger.log(log_message="Column is not present in file")
        except Exception as e:
            print('Exception occured while selecting column for review test \t', str(e))
            self.logger.log(log_message="Exception occured while selecting column for review test \t{0}".format(str(e)))

    def convert_Series_to_List(self,pandas_series):
        try:
            self.logger.log(log_message="converting pandas series to list")
            properties=pandas_series.tolist()
            return properties
        except Exception as e:
            print('Exception occured while converting pandas series {0} to list {1}'.format(pandas_series,str(e)))
            self.logger.log(log_message="Error occured while converting pandas series to list \t{0}".format(str(e)))



    # def round_Brackets_Check(self,Testable_Column,iteration_value):
    def round_Brackets_Check(self, Testable_property):
        try:
            self.logger.log(log_message="Checking the total round brackets in {0}".format(Testable_property))
            count_opening_brackets = 0
            count_closing_brackets = 0
            # i=iteration_value
            # for i in range(len(Testable_Column)):
            # count_opening_brackets = count_opening_brackets + Testable_Column[i].count('(')
            # count_closing_brackets = count_closing_brackets + Testable_Column[i].count(')')
            count_opening_brackets = count_opening_brackets + Testable_property.count('(')
            count_closing_brackets = count_closing_brackets + Testable_property.count(')')

            if count_opening_brackets == count_closing_brackets:
                return True
            else:
                return False

        except Exception as e:
            print('Exception occured while checking the round brackets for {0} --- {1}'.format(Testable_property,str(e)))
            self.logger.log(log_message='Exception occured while checking the round brackets for {0} --- {1}'.format(Testable_property,str(e)))


    def square_Brackets_Check(self, Testable_property):
        try:
            self.logger.log(log_message="Checking the total square brackets in {0}".format(Testable_property))
            count_opening_brackets = 0
            count_closing_brackets = 0
            count_opening_brackets = count_opening_brackets + Testable_property.count('[')
            count_closing_brackets = count_closing_brackets + Testable_property.count(']')

            if count_opening_brackets == count_closing_brackets:
                return True
            else:
                return False

        except Exception as e:
            print('Exception occured while checking the square brackets for {0} --- {1}'.format(Testable_property,str(e)))
            self.logger.log(log_message='Exception occured while checking the square brackets for {0} --- {1}'.format(
                Testable_property, str(e)))


        def square_Brackets_Presence(self,Testable_property):
            try:
                self.logger.log(log_message="Checking the presence of square brackets in {0}".format(Testable_property))
                presence_of_square_brackets=0
                presence_of_square_brackets += Testable_property.count('[')
                presence_of_square_brackets += Testable_property.count(']')

                if presence_of_square_brackets == 0:
                    return False
                else:
                    return True

            except Exception as e:
                print('Exception occured while checking the presence of square brackets for {0} --- {1}'.format(Testable_property,str(e)))
                self.logger.log(log_message='Exception occured while checking the square brackets for {0} --- {1}'.format(Testable_property, str(e)))

    def asterisk_Check(self,Testable_property):
        try:
            self.logger.log(log_message="Checking the presence of asterisk in {0}".format(Testable_property))
            pattern=re.compile(r'//\*')
            match = pattern.search(Testable_property)
            if match:
               return True
            else:
               return False

        except Exception as e:
            print('Exception occured while checking the asterisk in {0} --- {1}'.format(Testable_property, str(e)))
            self.logger.log(log_message="Exception occured while checking the asterisk in {0} --- {1}".format(Testable_property, str(e)))


    def single_Slash_Start_Check(self,Testable_property):
        try:
            self.logger.log(log_message="Checking whether xpath {0} starts from single slash".format(Testable_property))
            pattern=re.compile(r'^/[A-Za-z]')
 #           pattern=re.compile(r'^/["html"]')
            match = pattern.search(Testable_property)
            if match:
                return True
            else:
                return False
        except Exception as e:
            print('Exception occured while checking if xpath starts from single slash  {0} --- {1}'.format(Testable_property, str(e)))
            self.logger.log(log_message="Exception occured while checking if xpath starts from single slash  {0} --- {1}".format(Testable_property, str(e)))

    def single_Quotes_Check(self,Testable_property):
        try:
            self.logger.log(log_message="Checking the count of single quotes in {0}".format(Testable_property))
            count_of_single_quotes=Testable_property.count('\'')

            if count_of_single_quotes % 2 == 0:
                return True
            else:
                return False

        except Exception as e:
            print('Exception occured while checking the single quotes in {0} --- {1}'.format(Testable_property, str(e)))
            self.logger.log(log_message="Exception occured while checking the single quotes in {0} --- {1}".format(Testable_property, str(e)))

    def double_Quotes_Check(self,Testable_property):
        try:
            self.logger.log(log_message="Checking the count of double quotes in {0}".format(Testable_property))
            count_of_double_quotes=Testable_property.count('\"')

            if count_of_double_quotes % 2 == 0:
                return True
            else:
                return False

        except Exception as e:
            print('Exception occured while checking the single quotes in {0} --- {1}'.format(Testable_property, str(e)))
            self.logger.log(log_message="Exception occured while checking the double quotes in {0} --- {1}".format(Testable_property, str(e)))

    def only_a_Word_Check(self,Testable_property):
        try:
            self.logger.log(log_message="Checking if the xpath {0} is just a word".format(Testable_property))
            only_word_present=Testable_property.isalpha()
            if only_word_present:
                return False
            else:
                return True
        except Exception as e:
            print('Exception occured while checking if only a single word is present {0} --- {1}'.format(Testable_property, str(e)))
            self.logger.log(log_message="Error occured while checking if the xpath {0} is just a word {1}".format(Testable_property,str(e)))

    def single_Slashes_Check(self,Testable_property):
        try:
            self.logger.log("Counting the single slashes in {0}".format(Testable_property))
            count_of_single_slashes=0
            patt = re.compile(r'[a-zA-Z0-9]\/[a-zA-Z0-9]')
            match = patt.finditer(Testable_property)
            for match in match:
                count_of_single_slashes += 1

            print("The single slash count = {0}".format(count_of_single_slashes))
            return count_of_single_slashes
        except Exception as e:
            print('Exception occured while checking the single slashes in {0} --- {1}'.format(Testable_property, str(e)))
            self.logger.log(log_message="Exception occured while checking the single slashes in {0} --- {1}".format(Testable_property,str(e)))


    def single_Slashes_presence(self, Testable_property):
        try:
            # count_of_single_slashes = 0
            # patt = re.compile(r'[a-zA-Z0-9]\/[a-zA-Z0-9]')
            # match = patt.finditer(Testable_property)
            self.logger.log("Checking the presence of slashes in {0}".format(Testable_property))
            match=Testable_property.count('/')
            if match > 0:
                return True
            else:
                return False

        except Exception as e:
            print('Exception occured while checking the single slashes in {0} --- {1}'.format(Testable_property, str(e)))
            self.logger.log(log_message="Exception occured while checking the presence of slashes in {0} --- {1}".format(Testable_property,str(e)))


    def double_Slashes_Check(self, Testable_property):
        try:
            self.logger.log("Counting the double slashes in {0}".format(Testable_property))
            count_of_double_slashes=0
            patt = re.compile(r'[a-zA-Z0-9]\//[a-zA-Z0-9]')
            match = patt.finditer(Testable_property)
            for match in match:
                count_of_double_slashes += 1

            print("The double slash count = {0}".format(count_of_double_slashes))
            return count_of_double_slashes
        except Exception as e:
            print('Exception occured while checking the single slashes in {0} --- {1}'.format(Testable_property, str(e)))
            self.logger.log(log_message="Exception occured while counting the double slashes in {0} --- {1}".format(Testable_property,str(e)))


    def double_Slashes_presence(self, Testable_property):
        try:
            self.logger.log("Checking the presence of slashes in {0}".format(Testable_property))
            patt = re.compile(r'[a-zA-Z0-9]\//[a-zA-Z0-9]')
            match = patt.finditer(Testable_property)
            if match:
                return True
            else:
                return False

        except Exception as e:
            print('Exception occured while checking the single slashes in {0} --- {1}'.format(Testable_property, str(e)))
            self.logger.log(log_message="Exception occured while checking the presence of slashes in {0} --- {1}".format(Testable_property,str(e)))


    def check_xpath_starting(self,Testable_property):
        try:
            self.logger.log("Checking if xpath {0} starts from alphanumeric".format(Testable_property))
            pattern = re.compile("^[A-Za-z0-9]")
            match = pattern.search(Testable_property)
            if match:
            #    print("broken")
                 return False
            else:
            #    print("Not broken")
                 return True

        except Exception as e:
            print('Exception occured while checking the single slashes in {0} --- {1}'.format(Testable_property, str(e)))
            self.logger.log(log_message="Exception occured while checking if xpath {0} starts from alphanumeric --- {1}".format(Testable_property,str(e)))


    def review_Decider(self,round_bracket_check,square_bracket_check,single_quotes_check,double_quotes_check,asterisk_check,single_slash_start_check,single_slashes_presence):
        try:
            # if single_slashes_presence is True or double_slashes_presence is True:
            #     slashes_presence = True
            # else:
            #     slashes_presence = False
            self.logger.log(log_message="Started the review decider function")
            broken_xpath = [round_bracket_check, square_bracket_check, single_quotes_check, double_quotes_check, single_slashes_presence]
            if all(broken_xpath):
                message1 = "xpath Looks fine"
            else:
                message1 = "xpath is broken"

            # if single_slashes_check > 4 or double_slashes_check > 4 and asterisk_check == True:
            #     message2="Looks like an absolute xpath, please use less slashes and try to avoid //*."
            # elif single_slashes_check > 4 or double_slashes_check > 4 and asterisk_check == False:
            #     message2=" Looks like an absolute xpath, please try not to use absolute xpath"
            # elif single_slashes_check < 4 or double_slashes_check < 4 and asterisk_check == True:
            #     message2="Please avoid the usage of * in xpath"
            # else:
            #     message2="Looks fine"

            if single_slash_start_check is True and asterisk_check is True:
                message2="Looks like an absolute xpath. Please try to avoid xpath starting with single slashes or //*."
            elif single_slash_start_check is False and asterisk_check is True:
                message2 = "Please try to avoid xpath with //*."
            elif single_slash_start_check is True and asterisk_check is False:
                message2 = "Looks like an absolute xpath. Please try to avoid xpath starting with single slashes"
            else:
                message2 = "No suggestions"

            return message1,message2
        except Exception as e:
            print('Exception occured while deciding review messages',str(e))
            self.logger.log(log_message="Exception occured while deciding the review messages {0}".format(str(e)))


    def blank_Rows_Dealer(self,dataframe,null_column,review_column,suggestions_column):
        try:
            self.logger.log(log_message="Dealing with the empty rows of xpath column")
            dataframe.loc[dataframe[null_column].isna(),[review_column]]="No xpath found"
            dataframe.loc[dataframe[null_column].isna(), [suggestions_column]] = "No suggestions"
        except Exception as e:
            print('Exception occured while dealing with blank xpaths', str(e))
            self.logger.log(log_message="Exception occured while dealing with blank rows of xpath column {0}".format(str(e)))

    def integers_Dealer(self,dataframe,column_to_be_checked,review_column,suggestions_column):
        try:
            self.logger.log(log_message="Dealing with the integer rows of xpath column")
            dataframe.loc[dataframe[column_to_be_checked].apply(type) == int, [review_column]] = "No xpath, only integers found"
            dataframe.loc[dataframe[column_to_be_checked].apply(type) == int, [suggestions_column]] = "Please add proper xpath"

        except Exception as e:
            print('Exception occured while dealing with Integers/numericals inplace of xpaths', str(e))
            self.logger.log(log_message="Exception occured while dealing with integer rows of xpath column {0}".format(str(e)))

    def review_Writer(self,message1,message2,dataframe,review_column,suggestion_column,row):
        try:
            # if message1 == "Looks fine" and message2 == "No suggestion":
            #     dataframe[review_column][row]='xpath looks fine'
            #     dataframe[suggestion_column][row]='No suggestion'
            # else:
            self.logger.log(log_message="Writing the reviews to the updated dataframe")
            dataframe[review_column][row]=message1
            dataframe[suggestion_column][row]=message2

            if dataframe[review_column][row] == 'xpath is broken' and dataframe[suggestion_column][row] == 'No suggestions':
                dataframe[suggestion_column][row]='Some parenthesis/brackets/quotes/html tags missing'

            elif dataframe[review_column][row] == 'xpath is broken' and dataframe[suggestion_column][row] != 'No suggestions':
                dataframe[suggestion_column][row]='Some parenthesis/brackets/quotes missing' + ', '+message2

            else:
                pass
        except Exception as e:
            print('Exception occured while writing review to dataframe', str(e))
            self.logger.log(log_message="Exception occured while writing the reviews to the updated dataframe {0}".format(str(e)))


    def convert_dataframe_to_Resource(self,dataframe):
        try:
            self.logger.log(log_message="Converting the updated dataframe to resource file")
            time=datetime.now().strftime("%d_%m_%Y-%I_%M_%S_%p")
            filename="Reviewed_files/Xpath_Reviewed_"+time+".xlsx"
 #           filename = "Xpath_Reviewed_" + time + ".xlsx"


            dataframe.to_excel(filename)

        except Exception as e:
            print('Exception occured while converting the reviewed dataframe to xlsm file', str(e))
            self.logger.log(log_message="Error occured while converting the updated dataframe to resource file {0}".format(str(e)))

    def add_File_To_Directory(self,directory_path,file_Instance):
        try:
            self.logger.log(log_message="Storing the input file {0} to the directory {1}".format(file_Instance.filename,directory_path))
            time = datetime.now().strftime("%d_%m_%Y-%I_%M_%S_%p")
            filename = time + '_' + file_Instance.filename
            file_Instance.save(os.path.join(directory_path, secure_filename(filename)))

        except Exception as e:
            print('Exception occured while adding the file to {0} {1}'.format(directory_path, str(e)))
            self.logger.log(log_message="Exception occured while storing the input file {0} to the directory {1}".format(file_Instance.filename,directory_path))

    def fetch_Latest_File_From_Directory(self,directory_path):
        try:
            self.logger.log(log_message="fetching the latest file from directory {0} for downloading".format(directory_path))
            file = os.listdir(directory_path)
            paths = [os.path.join(directory_path, basename) for basename in file]
            return max(paths, key=os.path.getctime)

        except Exception as e:
            print('Exception occured while fetching the latest file from {0} {1}'.format(directory_path,str(e)))
            self.logger.log(log_message="fetching the latest file from directory {0} for downloading {1}".format(directory_path,str(e)))

    def add_File_To_Cloud(self,folder_name,bucket_name,file_Instance,storage_client):
        try:
            self.logger.log(log_message="adding the user input file to the google cloud")
            bucket = storage_client.get_bucket(bucket_name)
            time = datetime.now().strftime("%d_%m_%Y-%I_%M_%S_%p")
            filename = time + '_' + file_Instance.filename
            blob=bucket.blob(folder_name+'/'+filename)
        #    blob.upload_from_filename(file_Instance)
            blob.upload_from_file(file_Instance)

        except Exception as e:
            print('Exception occured while the uploding file from {0} google bucket folder {1}'.format(folder_name, str(e)))
            self.logger.log(log_message="Exception occured while the uploding file from {0} google bucket folder {1}".format(folder_name,
                                                                                                     str(e)))

import pandas as pd
import re
from Custom_Exceptions import EmptyFileException

class back_Operations():
    def file_Reader(self,filename):
        """ This method just reads the input file from the location"""
        try:
            fname=filename
            dataframe=pd.read_excel(fname,sheet_name='Object repository')
            return dataframe
        except Exception as e:
            print('Exception occured while reading the file \t',str(e))

    def check_File_empty(self,dataframe):
        try:
            is_empty=dataframe.empty
            if is_empty:
                raise EmptyFileException()
            else:
                return dataframe
        except Exception as e:
            print('Exception occured while checking if the file is empty - \t', str(e))

    def create_Review_Columns(self,dataframe):
        """ This method adds the review column in the existing dataframe"""
        try:
            review_column_name='Auto Code Review'
            review_suggestion='Review Suggestions'
            dataframe[review_column_name]=''
            dataframe[review_suggestion]=''
            updated_dataframe=dataframe
            return updated_dataframe,review_column_name,review_suggestion
        except Exception as e:
            print('Exception occured while creating the review columns \t', str(e))


    def select_Column_For_Test(self,dataframe,column_name):
        try:
            if column_name in dataframe.columns:
               Testable_Column= dataframe[column_name]
               return Testable_Column
            else:
                return "Column is not present in file"
        except Exception as e:
            print('Exception occured while selecting column for review test \t', str(e))

    def convert_Series_to_List(self,pandas_series):
        try:
            properties=pandas_series.tolist()
            return properties
        except Exception as e:
            print('Exception occured while converting pandas series {0} to list {1}'.format(pandas_series,str(e)))



    # def round_Brackets_Check(self,Testable_Column,iteration_value):
    def round_Brackets_Check(self, Testable_property):
        try:
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


    def square_Brackets_Check(self, Testable_property):
        try:
            count_opening_brackets = 0
            count_closing_brackets = 0
            count_opening_brackets = count_opening_brackets + Testable_property.count('[')
            count_closing_brackets = count_closing_brackets + Testable_property.count(']')

            if count_opening_brackets == count_closing_brackets:
                return True
            else:
                return False

        except Exception as e:
            print('Exception occured while checking the round brackets for {0} --- {1}'.format(Testable_property,str(e)))


    def asterisk_Check(self,Testable_property):
        try:
            pattern=re.compile(r'//\*')
            match = pattern.search(Testable_property)
            if match:
               return True
            else:
               return False

        except Exception as e:
            print('Exception occured while checking the asterisk in {0} --- {1}'.format(Testable_property, str(e)))


    def single_Slash_Start_Check(self,Testable_property):
        try:
            pattern=re.compile(r'^/[A-Za-z]')
            match = pattern.search(Testable_property)
            if match:
                return True
            else:
                return False
        except Exception as e:
            print('Exception occured while checking if xpath starts from single slash  {0} --- {1}'.format(Testable_property, str(e)))

    def single_Quotes_Check(self,Testable_property):
        try:
            count_of_single_quotes=Testable_property.count('\'')

            if count_of_single_quotes % 2 == 0:
                return True
            else:
                return False

        except Exception as e:
            print('Exception occured while checking the single quotes in {0} --- {1}'.format(Testable_property, str(e)))

    def double_Quotes_Check(self,Testable_property):
        try:
            count_of_double_quotes=Testable_property.count('\"')

            if count_of_double_quotes % 2 == 0:
                return True
            else:
                return False

        except Exception as e:
            print('Exception occured while checking the single quotes in {0} --- {1}'.format(Testable_property, str(e)))


    def single_Slashes_Check(self,Testable_property):
        try:
            count_of_single_slashes=0
            patt = re.compile(r'[a-zA-Z0-9]\/[a-zA-Z0-9]')
            match = patt.finditer(Testable_property)
            for match in match:
                count_of_single_slashes += 1

            print("The single slash count = {0}".format(count_of_single_slashes))
            return count_of_single_slashes
        except Exception as e:
            print('Exception occured while checking the single slashes in {0} --- {1}'.format(Testable_property, str(e)))

    def double_Slashes_Check(self, Testable_property):
        try:
            count_of_double_slashes=0
            patt = re.compile(r'[a-zA-Z0-9]\//[a-zA-Z0-9]')
            match = patt.finditer(Testable_property)
            for match in match:
                count_of_double_slashes += 1

            print("The double slash count = {0}".format(count_of_double_slashes))
            return count_of_double_slashes
        except Exception as e:
            print('Exception occured while checking the single slashes in {0} --- {1}'.format(Testable_property, str(e)))

    def review_Decider(self,round_bracket_check,square_bracket_check,single_quotes_check,double_quotes_check,asterisk_check,single_slash_start_check):
        try:
            broken_xpath=[round_bracket_check,square_bracket_check,single_quotes_check,double_quotes_check]
            if all(broken_xpath):
                message1="xpath Looks fine"
            else:
                message1="xpath is broken"

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
                message2 = "No suggestion"

            return message1,message2
        except Exception as e:
            print('Exception occured while deciding review messages',str(e))


    def blank_Rows_Dealer(self,dataframe,null_column,review_column,suggestions_column):
        try:
            dataframe.loc[dataframe[null_column].isna(),[review_column]]="No xpath found"
            dataframe.loc[dataframe[null_column].isna(), [suggestions_column]] = "No suggestions"
        except Exception as e:
            print('Exception occured while dealing with blank xpaths', str(e))

    def review_Writer(self,message1,message2,dataframe,review_column,suggestion_column,row):
        try:
            # if message1 == "Looks fine" and message2 == "No suggestion":
            #     dataframe[review_column][row]='xpath looks fine'
            #     dataframe[suggestion_column][row]='No suggestion'
            # else:
            dataframe[review_column][row]=message1
            dataframe[suggestion_column][row]=message2

            if dataframe[review_column][row] == 'xpath is broken' and dataframe[suggestion_column][row] == 'No suggestion':
                dataframe[suggestion_column][row]='Some parenthesis/brackets/quotes missing'

            elif dataframe[review_column][row] == 'xpath is broken' and dataframe[suggestion_column][row] != 'No suggestion':
                dataframe[suggestion_column][row]='Some parenthesis/brackets/quotes missing'+', '+message2

            else:
                pass
        except Exception as e:
            print('Exception occured while writing review to dataframe', str(e))


    def convert_dataframe_to_Resource(self,dataframe):
        try:
            filename='Reviewed files/Xpath_Reviewed.xlsx'
            dataframe.to_excel(filename)

        except Exception as e:
            print('Exception occured while converting the reviewed dataframe to xlsm file', str(e))
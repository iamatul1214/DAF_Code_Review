import pandas as pd
import re

class back_Operations():
    def file_Reader(self,filename):
        """ This method just reads the input file from the location"""
        try:
            fname=filename
            dataframe=pd.read_excel(fname)
            return dataframe
        except Exception as e:
            print('Exception occured while reading the file \t',str(e))


    def create_Review_Column(self,dataframe):
        """ This method adds the review column in the existing dataframe"""
        try:
            review_column_name='Auto Review Comments'
            dataframe[review_column_name]=''
            updated_dataframe=dataframe
            return updated_dataframe
        except Exception as e:
            print('Exception occured while creating the review column \t', str(e))


    def select_Column_For_Test(self,dataframe,column_name):
        try:
            if column_name in dataframe.columns:
               Testable_Column= dataframe[column_name]
               return Testable_Column
            else:
                return "Column is not present in file"
        except Exception as e:
            print('Exception occured while selecting column for review test \t', str(e))


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
               return False
            else:
               return True

        except Exception as e:
            print('Exception occured while checking the asterisk in {0} --- {1}'.format(Testable_property, str(e)))

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


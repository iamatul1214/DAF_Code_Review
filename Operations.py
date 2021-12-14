import pandas as pd

class back_Operations():
    def file_Reader(filename,):
        """ This method just reads the input file from the location"""
        try:
            fname=filename
            dataframe=pd.read_excel(fname)
            return dataframe
        except Exception as e:
            print('Exception occured while reading the file \t',str(e))


    def create_Review_Column(dataframe):
        """ This method adds the review column in the existing dataframe"""
        try:
            review_column_name='Auto Review Comments'
            dataframe[review_column_name]=''
            updated_dataframe=dataframe
            return updated_dataframe
        except Exception as e:
            print('Exception occured while creating the review column \t', str(e))


    def select_Column_For_Test(dataframe,column_name):
        try:
            if column_name in dataframe.columns:
               Testable_Column= dataframe[column_name]
               return Testable_Column
            else:
                return "Column is not present in file"
        except Exception as e:
            print('Exception occured while selecting column for review test \t', str(e))



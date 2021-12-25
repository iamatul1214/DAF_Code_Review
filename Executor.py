import pandas as pd
from Operations import back_Operations
from datetime import datetime

# bo=back_Operations()
class Executor():
    def __init__(self):
        self.bo=back_Operations()

    def execute(self, file):
        try:
            filename=file

            #filename='Testing files/Resource.xlsm'

            column_name='Properties'
            # bo.add_File_To_Directory(directory_path=directory_path,file_Instance=filename)
            dataframe=self.bo.file_Reader(filename=filename)
            dataframe=self.bo.check_File_empty(dataframe=dataframe)
            updated_dataframe,review_columm,review_suggestion=self.bo.create_Review_Columns(dataframe=dataframe)
            Testable_Column=self.bo.select_Column_For_Test(dataframe=updated_dataframe,column_name=column_name)
            properties=self.bo.convert_Series_to_List(updated_dataframe[column_name])

            for i in range(len(properties)):
                properties[i]=str(properties[i])
                if properties[i] != 'nan':
                    round_brackets= self.bo.round_Brackets_Check(Testable_property=properties[i])
                    square_brackets= self.bo.square_Brackets_Check(Testable_property=properties[i])
                    asterisk= self.bo.asterisk_Check(Testable_property=properties[i])
                    single_quotes= self.bo.single_Quotes_Check(Testable_property=properties[i])
                    double_quotes= self.bo.double_Quotes_Check(Testable_property=properties[i])
                    single_slash_start= self.bo.single_Slash_Start_Check(Testable_property=properties[i])
                    single_slash_presence=self.bo.single_Slashes_presence(Testable_property=properties[i])
                    # double_slash_presence = bo.double_Slashes_presence(Testable_property=properties[i])

                    message1,message2=self.bo.review_Decider(round_bracket_check=round_brackets,square_bracket_check=square_brackets,
                                                        single_quotes_check=single_quotes,double_quotes_check=double_quotes,asterisk_check=asterisk,
                                                        single_slash_start_check=single_slash_start,single_slashes_presence=single_slash_presence)
                    self.bo.review_Writer(message1=message1,message2=message2,dataframe=updated_dataframe,review_column=review_columm,
                                     suggestion_column=review_suggestion,row=i)

                   # bo.blank_Rows_Dealer(dataframe=updated_dataframe,null_column=column_name,review_column=review_columm,suggestions_column=review_suggestion)
                else:
                    pass
            self.bo.blank_Rows_Dealer(dataframe=updated_dataframe, null_column=column_name, review_column=review_columm,
                                 suggestions_column=review_suggestion)
            self.bo.integers_Dealer(dataframe=updated_dataframe,column_to_be_checked=column_name,review_column=review_columm,
                               suggestions_column=review_suggestion)
            self.bo.convert_dataframe_to_Resource(dataframe=updated_dataframe)

        except Exception as e:
             print("Error occured while reading the filename\t", filename)


    def fetch_latest_file(self,directory_path):
        download_file=self.bo.fetch_Latest_File_From_Directory(directory_path=directory_path)
        return download_file

    def add_File_to_Directory(self,directory_path,file):
        self.bo.add_File_To_Directory(directory_path=directory_path, file_Instance=file)
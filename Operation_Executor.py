from Operations import back_Operations

class Executor():
    def instantiate_Operations(self):
        try:
            bo = back_Operations()
            return bo
        except Exception as e:
            print("Error occured while creating object of Operations class\t",str(e))

    def file_PreChecks(self,Operation_class_instance):
        try:
            filename = 'Testing files/Resource.xlsm'
            column_name = 'Properties'
            dataframe = Operation_class_instance.file_Reader(filename=filename)
            dataframe = Operation_class_instance.check_File_empty(dataframe=dataframe)
        except Exception as e:
            print("Error occured while creating object of Operations class\t", str(e))
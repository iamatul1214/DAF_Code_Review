from google.cloud import storage
import os

input_file="C:\\Users\\atulkumarrai\\PycharmProjects\\Ineuron practice\\Ineuron_practice\\DAF_Code_Review\\Testing files\\Resource2.xlsm"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'auto-xpath-reviewer-bd20b4ff36c3.json'
client = storage.Client()
print(dir(client))

bucket = client.get_bucket('daf_code_review')
print(bucket.path)
blob=bucket.blob('Input_Resource_Files/28_12_2021-06_39_50_PM_Resource2.xlsm')
blob.upload_from_filename(input_file)


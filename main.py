import json
from flask import Flask, render_template,request,send_file,send_from_directory, redirect
from Executor import Executor
from google.cloud import storage
import os

# os.putenv('LANG', 'en_US.UTF-8')
# os.putenv('LC_ALL', 'en_US.UTF-8')

# bo = back_Operations()
e = Executor()

with open('config.json','r') as config:
    params=json.load(config)["Params"]

app=Flask(__name__)
app.config["UPLOAD_FOLDER"] = params["Upload_Local_Location"]
app.config["Allowed_Extensions"]=params["File_Extensions"]
app.config["File_Type_Error"]=params["Invalid_File_Error"]
app.config["No_File_Error"]=params["No_File_Error"]
app.config["Download_Folder"]=params["Reviewed_Files_Folder"]
app.config["Bucket_Name"]=params["Bucket_Name"]
app.config["Auto_Review_Plots_Dir"]=params["Review_Plots_Folder"]
app.config["Suggestions_Plots_Dir"]=params["Suggestions_Plots_Folder"]
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'auto-xpath-reviewer-bd20b4ff36c3.json'

def check_file_extension(filename):
    return filename.split(".")[-1] in app.config["Allowed_Extensions"]


@app.route("/",methods=['GET'])
def home():
    return render_template('Welcome.html')


@app.route('/reviewing',methods=['GET','POST'])
def start_Review():
    try:
        if request.method == 'POST':
            f = request.files['ResourceFile']
            if f:
                if check_file_extension(f.filename):
                    client = storage.Client()
                    e.add_File_to_Directory(directory_path=app.config["UPLOAD_FOLDER"],file=f)
                    # e.add_File_To_Cloud(folder_name=app.config["UPLOAD_FOLDER"],file_Instance=f,
                    #                     bucket_name=app.config["Bucket_Name"],storage_client=client)
                    e.execute(file=f)
                else:
                    return render_template("Welcome.html",File_Error=app.config["File_Type_Error"])
                return render_template("results.html")
            else:
                return render_template("Welcome.html",File_Error=app.config["No_File_Error"])

    except Exception as ex:
        print("Error occured\t",str(ex))
        return render_template("Exception.html")

@app.route('/download', methods=['GET','POST'])
def download_File():
    try:
        download_File=e.fetch_latest_file(directory_path=app.config["Download_Folder"])
        return send_file(download_File)
    except Exception as ex:
        print("Error occured\t", str(ex))
        return render_template("Exception.html")

@app.route('/analysis',methods=['GET','POST'])
def reports_Analysis():
    try:
        plots=e.result_Analysis()
        review_plot=e.fetch_latest_file(directory_path=app.config["Auto_Review_Plots_Dir"])
        suggestion_plot=e.fetch_latest_file(directory_path=app.config["Suggestions_Plots_Dir"])
        graphs=[review_plot,suggestion_plot]
        return render_template("fileAnalysis.html",name="review plots",url=graphs)
    except Exception as ex:
        print("Error occured\t",str(ex))
        return render_template("Exception.html")



if __name__=="__main__":
    app.run(debug=True)
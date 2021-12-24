import json
from flask import Flask, render_template,request,send_file,send_from_directory, redirect
from Executor import Executor
from Operations import back_Operations



bo = back_Operations()
e = Executor()

with open('config.json','r') as config:
    params=json.load(config)["Params"]
app=Flask(__name__)

app.config["UPLOAD_FOLDER"] = params["Upload_Location"]
app.config["Allowed_Extensions"]=params["File_Extensions"]
app.config["File_Type_Error"]=params["Invalid_File_Error"]
app.config["No_File_Error"]=params["No_File_Error"]
app.config["Download_Folder"]=params["Reviewed_Files_Folder"]

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
                    bo.add_File_To_Directory(directory_path=app.config["UPLOAD_FOLDER"],file_Instance=f)
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
        download_File=bo.fetch_Latest_File_From_Directory(directory_path=app.config["Download_Folder"])
        return send_file(download_File)
    except Exception as ex:
        print("Error occured\t", str(ex))
        return render_template("Exception.html")




if __name__=="__main__":
    app.run(debug=True)
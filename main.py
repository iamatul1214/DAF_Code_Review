import json
from datetime import datetime
from flask import Flask, render_template
from flask import request, redirect
from werkzeug.utils import secure_filename
from Executor import Executor
import pandas as pd
import os

e=Executor()

with open('config.json','r') as config:
    params=json.load(config)["Params"]
app=Flask(__name__)

app.config["UPLOAD_FOLDER"] = params["Upload_Location"]
@app.route("/",methods=['GET'])
def home():
    return render_template('Welcome.html')


@app.route('/reviewing',methods=['GET','POST'])
def start_Review():
    if request.method == 'POST':
        f = request.files['ResourceFile']
        if f:
            time = datetime.now().strftime("%d_%m_%Y-%I_%M_%S_%p")
            filename=time+'_'+f.filename
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename)))


            e.execute(file=f)
            return "work in progress"
        else:
            return render_template("Welcome.html",File_Error="No file uploaded. Please upload a file.")






if __name__=="__main__":
    app.run(debug=True)
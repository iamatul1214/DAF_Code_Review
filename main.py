from flask import Flask, render_template
from flask import request, redirect


app=Flask(__name__)


@app.route("/",methods=['GET'])
def home():
    return render_template('Welcome.html')


@app.route('/reviewing',methods=['GET','POST'])
def start_Review():
    if request.method == 'POST':
        f = request.form['ResourceFile']
        print("file=",f)






if __name__=="__main__":
    app.run(debug=True)
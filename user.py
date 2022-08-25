from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

headings = ("ID", "USER", "NUMBER")
data = (
    ("1","Alice","0123"),
    ("2","Roy Bob","0456"),
    ("3","Mac","0789"),
    ("4","Alice","0123"),
    ("5","Roy Bob","0456"),
    ("6","Mac","0789"),
)

@app.route("/")
def user():
    #if request.method == 'POST':
    #   try:
            #ID = request.form['ID']
            #USER = request.form['USER']
            #NUMBER = request.form['NUMBER']
            #dataset = [ID, USER, NUMBER]
            #dataArray = np.array(dataset)
            title = "Flask Assignment"
    #    except ValueError:
    #        return "Please Enter Valaid Information"
            return render_template("user.html", title=title, headings=headings, data=data) 

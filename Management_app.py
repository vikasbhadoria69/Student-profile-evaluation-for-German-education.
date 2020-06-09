from flask import Flask, render_template,request
app = Flask(__name__,template_folder='template')
import pickle
import numpy as np
from random import randint


file = open('Management-better.pkl', 'rb')
model = pickle.load(file)
file.close()

@app.route('/', methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        myDict=request.form
        Aggregate=float(myDict['Aggregate'])
        WorkExperienceless1=int(myDict['WorkExperienceless1'])
        Private=int(myDict['Private'])
        WorkExperienceMore1=int(myDict['WorkExperienceMore1'])
        GRE=int(myDict['GRE'])
        Germanlevel=int(myDict['Germanlevel'])
        

        
        inputFeatures=[[Aggregate,WorkExperienceless1,Private,WorkExperienceMore1,GRE,Germanlevel]]
        admission_prob=model.predict_proba(inputFeatures)[:,1]
        admission_prob=admission_prob*100
        print(admission_prob)
        if admission_prob < 10:
            return render_template("show.html",inf=str(randint(9,15)))
        elif 10 < admission_prob < 20:
            return render_template("show.html",inf=str(randint(15,22)))
        elif 20 < admission_prob < 30:
            return render_template("show.html",inf=str(randint(23,32)))
        elif 30 < admission_prob < 40:
            return render_template("show.html",inf=str(randint(33,42)))
        elif 40 < admission_prob < 50:
            return render_template("show.html",inf=str(randint(43,52)))
        elif 50 < admission_prob < 60:
            return render_template("show.html",inf=str(randint(53,62)))
        elif 60 < admission_prob < 70:
            return render_template("show.html",inf=str(randint(63,72)))
        elif 70 < admission_prob < 80:
            return render_template("show.html",inf=str(randint(73,82)))
        elif 80 < admission_prob < 95:
            return render_template("show.html",inf=str(randint(83,92)))
        elif 95 < admission_prob < 100:
            return render_template("show.html",inf=str(randint(93,98)))
    return render_template("index.html")
    #return 'Hello, World!' + str(infprob)

@app.route("/univlist")
def univlist():
    return render_template('Management_univ.html')


if __name__ == "__main__": 
    app.run(debug=True)
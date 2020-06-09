from flask import Flask, render_template,request
app = Flask(__name__,template_folder='template')
import pickle
from random import randint

file = open('Mecha_new_better-model.pkl', 'rb')
model = pickle.load(file)
file.close()

@app.route('/', methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        myDict=request.form
        Aggregate=float(myDict['Aggregate'])
        GRE=int(myDict['GRE'])
        Internship=int(myDict['Internship'])
        Germanlevel=int(myDict['Germanlevel'])
        DegreeCompleted=int(myDict['DegreeCompleted'])
        Project=int(myDict['Project'])

        
        inputFeatures=[[Aggregate,GRE,Internship,Germanlevel,DegreeCompleted,Project]]
        admission_prob=model.predict_proba(inputFeatures)[:,1]
        admission_prob=admission_prob*100
        print(admission_prob)
        if admission_prob < 10:
            return render_template("show.html",inf=str(randint(10,17)))
        elif 10 < admission_prob < 20:
            return render_template("show.html",inf=str(randint(18,27)))
        elif 20 < admission_prob < 30:
            return render_template("show.html",inf=str(randint(28,37)))
        elif 30 < admission_prob < 40:
            return render_template("show.html",inf=str(randint(38,47)))
        elif 40 < admission_prob < 50:
            return render_template("show.html",inf=str(randint(48,57)))
        elif 50 < admission_prob < 60:
            return render_template("show.html",inf=str(randint(58,67)))
        elif 60 < admission_prob < 70:
            return render_template("show.html",inf=str(randint(68,77)))
        elif 70 < admission_prob < 80:
            return render_template("show.html",inf=str(randint(78,87)))
        elif 80 < admission_prob < 95:
            return render_template("show.html",inf=str(randint(88,94)))
        elif 95 < admission_prob < 100:
            return render_template("show.html",inf=str(randint(95,98)))
            
    return render_template("index.html")
    
@app.route("/univlist")
def univlist():
    return render_template('Mechatronics_univ.html')

if __name__ == "__main__": 
    app.run(debug=True)
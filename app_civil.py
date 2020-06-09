from flask import Flask, render_template,request
app = Flask(__name__,template_folder='template')
import pickle
from random import randint

file = open('Civil_better.pkl', 'rb')
model = pickle.load(file)
file.close()

@app.route('/', methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        myDict=request.form
        Aggregate=float(myDict['Aggregate'])
        DegreeCompleted=int(myDict['DegreeCompleted'])
        Internship=int(myDict['Internship'])
        Germanlevel=int(myDict['Germanlevel'])
        GRE=int(myDict['GRE'])
        Winter=int(myDict['Winter'])

        
        inputFeatures=[[Aggregate,DegreeCompleted,Internship,Germanlevel,GRE,Winter]]
        admission_prob=model.predict_proba(inputFeatures)[:,1]
        admission_prob=admission_prob*100
        print(admission_prob)
        if admission_prob < 10:
            return render_template("show.html",inf=str(randint(10,15)))
        elif 10 < admission_prob < 20:
            return render_template("show.html",inf=str(randint(16,25)))
        elif 20 < admission_prob < 30:
            return render_template("show.html",inf=str(randint(26,34)))
        elif 30 < admission_prob < 40:
            return render_template("show.html",inf=str(randint(35,44)))
        elif 40 < admission_prob < 50:
            return render_template("show.html",inf=str(randint(45,54)))
        elif 50 < admission_prob < 60:
            return render_template("show.html",inf=str(randint(55,64)))
        elif 60 < admission_prob < 70:
            return render_template("show.html",inf=str(randint(65,74)))
        elif 70 < admission_prob < 80:
            return render_template("show.html",inf=str(randint(75,84)))
        elif 80 < admission_prob < 90:
            return render_template("show.html",inf=str(randint(85,90)))
        elif 90 < admission_prob < 100:
            return render_template("show.html",inf=str(randint(91,96)))
            
    return render_template("index.html")
    
@app.route("/univlist")
def univlist():
    return render_template('Civil_univ.html')

if __name__ == "__main__": 
    app.run(debug=True)
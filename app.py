from flask import Flask, render_template,request
app = Flask(__name__,template_folder='template')
import pickle
from random import randint

file1 = open('Chemical-model-better.pkl', 'rb')
file2 = open('Civil_better.pkl', 'rb')
file3 = open('DS_better.pkl', 'rb')
file4 = open('Electrical-model_better.pkl', 'rb')
file5 = open('Electronics-model-better.pkl', 'rb')
file6 = open('IT-better-model.pkl', 'rb')
file7 = open('Management-better.pkl', 'rb')
file8 = open('Material-model_better.pkl', 'rb')
file9 = open('Mecha_new_better-model.pkl', 'rb')
file10 = open('Mechanical-model-better.pkl', 'rb')
file11 = open('Engg-Mmgt-model-better.pkl', 'rb')
model1 = pickle.load(file1)
model2 = pickle.load(file2)
model3 = pickle.load(file3)
model4 = pickle.load(file4)
model5 = pickle.load(file5)
model6 = pickle.load(file6)
model7 = pickle.load(file7)
model8 = pickle.load(file8)
model9 = pickle.load(file9)
model10 = pickle.load(file10)
model11 = pickle.load(file11)
file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()
file8.close()
file9.close()
file10.close()
file11.close()

admission_prob = 0

@app.route('/')
def home():
    return render_template('Germany_web_app.html')

'''----------------------Chemical----------------------------'''

@app.route('/chemical', methods=["GET","POST"])
def chemical():
    if request.method=="POST":
        myDict=request.form
        Aggregate=float(myDict['Aggregate'])
        Internship=int(myDict['Internship'])
        GRE=int(myDict['GRE'])
        GermanLevel=int(myDict['GermanLevel'])
        IELTS7=int(myDict['IELTS7'])
        DegreeCompleted=int(myDict['DegreeCompleted'])
        

        
        inputFeatures=[[Aggregate,Internship,GRE,GermanLevel,IELTS7,DegreeCompleted]]
        admission_prob=model1.predict(inputFeatures)[0]
        print(admission_prob)
        if admission_prob < 10:
            return render_template("Chemicalshow.html",inf=(randint(9,15)))
        elif 10 < admission_prob < 20:
            return render_template("Chemicalshow.html",inf=(randint(15,22)))
        elif 20 < admission_prob < 30:
            return render_template("Chemicalshow.html",inf=(randint(23,32)))
        elif 30 < admission_prob < 40:
            return render_template("Chemicalshow.html",inf=(randint(33,42)))
        elif 40 < admission_prob < 50:
            return render_template("Chemicalshow.html",inf=(randint(43,52)))
        elif 50 < admission_prob < 60:
            return render_template("Chemicalshow.html",inf=(randint(53,62)))
        elif 60 < admission_prob < 70:
            return render_template("Chemicalshow.html",inf=(randint(63,72)))
        elif 70 < admission_prob < 80:
            return render_template("Chemicalshow.html",inf=(randint(73,79)))
        elif 80 < admission_prob < 95:
            return render_template("Chemicalshow.html",inf=(randint(80,92)))
        elif 95 < admission_prob < 100:
            return render_template("Chemicalshow.html",inf=(randint(93,97)))
    return render_template("chemical_index.html")

@app.route("/univlist_chemical")
def univlist_chemical():
    return render_template('Chemical_univ.html')

'''----------------------Civil----------------------------'''

@app.route('/civil', methods=["GET","POST"])
def civil():
    if request.method=="POST":
        myDict=request.form
        Aggregate=float(myDict['Aggregate'])
        DegreeCompleted=int(myDict['DegreeCompleted'])
        Internship=int(myDict['Internship'])
        Germanlevel=int(myDict['Germanlevel'])
        GRE=int(myDict['GRE'])
        Winter=int(myDict['Winter'])

        
        inputFeatures=[[Aggregate,DegreeCompleted,Internship,Germanlevel,GRE,Winter]]
        admission_prob=model2.predict_proba(inputFeatures)[:,1]
        admission_prob=admission_prob*100
        print(admission_prob)
        if admission_prob < 10:
            return render_template("Civil_show.html",inf=(randint(10,15)))
        elif 10 < admission_prob < 20:
            return render_template("Civil_show.html",inf=(randint(16,25)))
        elif 20 < admission_prob < 30:
            return render_template("Civil_show.html",inf=(randint(26,34)))
        elif 30 < admission_prob < 40:
            return render_template("Civil_show.html",inf=(randint(35,44)))
        elif 40 < admission_prob < 50:
            return render_template("Civil_show.html",inf=(randint(45,54)))
        elif 50 < admission_prob < 60:
            return render_template("Civil_show.html",inf=(randint(55,64)))
        elif 60 < admission_prob < 70:
            return render_template("Civil_show.html",inf=(randint(65,74)))
        elif 70 < admission_prob < 80:
            return render_template("Civil_show.html",inf=(randint(75,84)))
        elif 80 < admission_prob < 90:
            return render_template("Civil_show.html",inf=(randint(85,90)))
        elif 90 < admission_prob < 100:
            return render_template("Civil_show.html",inf=(randint(91,96)))
            
    return render_template("Civil_index.html")
    
@app.route("/univlist_civil")
def univlist_civil():
    return render_template('Civil_univ.html')
    
'''----------------------DataScience----------------------------'''

@app.route('/DataScience', methods=["GET","POST"])
def DataScience():
    if request.method=="POST":
        myDict=request.form
        Aggregate=float(myDict['Aggregate'])
        GRE=int(myDict['GRE'])
        Project=int(myDict['Project'])
        Germanlevel=int(myDict['Germanlevel'])
        Internship=int(myDict['Internship'])
        Credits=int(myDict['Credits'])

        
        inputFeatures=[[Aggregate,GRE,Project,Germanlevel,Internship,Credits]]
        admission_prob=model3.predict_proba(inputFeatures)[:,1]
        admission_prob=admission_prob*100
        print(admission_prob)
        if admission_prob < 10:
            return render_template("DS_show.html",inf=(randint(10,17)))
        elif 10 < admission_prob < 20:
            return render_template("DS_show.html",inf=(randint(18,27)))
        elif 20 < admission_prob < 30:
            return render_template("DS_show.html",inf=(randint(28,37)))
        elif 30 < admission_prob < 40:
            return render_template("DS_show.html",inf=(randint(38,47)))
        elif 40 < admission_prob < 50:
            return render_template("DS_show.html",inf=(randint(48,57)))
        elif 50 < admission_prob < 60:
            return render_template("DS_show.html",inf=(randint(58,67)))
        elif 60 < admission_prob < 70:
            return render_template("DS_show.html",inf=(randint(68,77)))
        elif 70 < admission_prob < 80:
            return render_template("DS_show.html",inf=(randint(78,87)))
        elif 80 < admission_prob < 95:
            return render_template("DS_show.html",inf=(randint(84,94)))
        elif 95 < admission_prob < 100:
            return render_template("DS_show.html",inf=(randint(95,98)))
            
    return render_template("DS_index.html")
    
@app.route("/univlist_DataScience")
def univlist_DataScience():
    return render_template('DS_univ.html')

'''----------------------Electrical----------------------------'''

@app.route('/Electrical', methods=["GET","POST"])
def Electrical():
    if request.method=="POST":
        myDict=request.form
        Aggregate=float(myDict['Aggregate'])
        GRE=int(myDict['GRE'])
        Internship=int(myDict['Internship'])
        DegCompleted=int(myDict['DegCompleted'])
        Winter=int(myDict['Winter'])
        GermanLevel=int(myDict['GermanLevel'])

        
        inputFeatures=[[Aggregate,GRE,Internship,DegCompleted,Winter,GermanLevel]]
        admission_prob=model4.predict_proba(inputFeatures)[:,1]
        admission_prob=admission_prob*100
        print(admission_prob)
        if admission_prob < 10:
            return render_template("Electrical_show.html",inf=(randint(10,15)))
        elif 10 < admission_prob < 20:
            return render_template("Electrical_show.html",inf=(randint(16,25)))
        elif 20 < admission_prob < 30:
            return render_template("Electrical_show.html",inf=(randint(26,34)))
        elif 30 < admission_prob < 40:
            return render_template("Electrical_show.html",inf=(randint(35,44)))
        elif 40 < admission_prob < 50:
            return render_template("Electrical_show.html",inf=(randint(45,54)))
        elif 50 < admission_prob < 60:
            return render_template("Electrical_show.html",inf=(randint(55,64)))
        elif 60 < admission_prob < 70:
            return render_template("Electrical_show.html",inf=(randint(65,74)))
        elif 70 < admission_prob < 80:
            return render_template("Electrical_show.html",inf=(randint(75,84)))
        elif 80 < admission_prob < 90:
            return render_template("Electrical_show.html",inf=(randint(85,90)))
        elif 90 < admission_prob < 100:
            return render_template("Electrical_show.html",inf=(randint(91,96)))
            
    return render_template("Electrical_index.html")
    
@app.route("/univlist_electrical")
def univlist_electrical():
    return render_template('Electrical_univ.html')

'''----------------------Electronics----------------------------'''


@app.route('/Electronics', methods=["GET","POST"])
def Electronics():
    if request.method=="POST":
        myDict=request.form
        Aggregate=float(myDict['Aggregate'])
        GRE=int(myDict['GRE'])
        Internship=int(myDict['Internship'])
        Germanlevel=int(myDict['Germanlevel'])
        Private=int(myDict['Private'])
        DegreeCompleted=int(myDict['DegreeCompleted'])

        
        inputFeatures=[[Aggregate,GRE,Internship,Germanlevel,Private,DegreeCompleted]]
        admission_prob=model5.predict_proba(inputFeatures)[:,1]
        admission_prob=admission_prob*100
        print(admission_prob)
        if admission_prob < 10:
            return render_template("Electronics_show.html",inf=(randint(10,17)))
        elif 10 < admission_prob < 20:
            return render_template("Electronics_show.html",inf=(randint(18,27)))
        elif 20 < admission_prob < 30:
            return render_template("Electronics_show.html",inf=(randint(28,37)))
        elif 30 < admission_prob < 40:
            return render_template("Electronics_show.html",inf=(randint(38,47)))
        elif 40 < admission_prob < 50:
            return render_template("Electronics_show.html",inf=(randint(48,57)))
        elif 50 < admission_prob < 60:
            return render_template("Electronics_show.html",inf=(randint(58,67)))
        elif 60 < admission_prob < 70:
            return render_template("Electronics_show.html",inf=(randint(68,77)))
        elif 70 < admission_prob < 80:
            return render_template("Electronics_show.html",inf=(randint(78,87)))
        elif 80 < admission_prob < 95:
            return render_template("Electronics_show.html",inf=(randint(88,94)))
        elif 95 < admission_prob < 100:
            return render_template("Electronics_show.html",inf=(randint(95,98)))
            
    return render_template("Electronics_index.html")
    
@app.route("/univlist_electronics")
def univlist_electronics():
    return render_template('Electronics_Univ.html')

'''----------------------Engg-Mmgt----------------------------'''

@app.route('/Engg_mmgt', methods=["GET","POST"])
def Engg_mmgt():
    if request.method=="POST":
        myDict=request.form
        Aggregate=float(myDict['Aggregate'])
        WorkExperience=int(myDict['WorkExperience'])
        Private=int(myDict['Private'])
        Internship=int(myDict['Internship'])
        GRE=int(myDict['GRE'])
        Germanlevel=int(myDict['Germanlevel'])
        

        
        inputFeatures=[[Aggregate,WorkExperience,Private,Internship,GRE,Germanlevel]]
        admission_prob=model11.predict_proba(inputFeatures)[:,1]
        admission_prob=admission_prob*100
        print(admission_prob)
        if admission_prob < 10:
            return render_template("Engg-mmgt_show.html",inf=(randint(9,15)))
        elif 10 < admission_prob < 20:
            return render_template("Engg-mmgt_show.html",inf=(randint(15,22)))
        elif 20 < admission_prob < 30:
            return render_template("Engg-mmgt_show.html",inf=(randint(23,32)))
        elif 30 < admission_prob < 40:
            return render_template("Engg-mmgt_show.html",inf=(randint(33,42)))
        elif 40 < admission_prob < 50:
            return render_template("Engg-mmgt_show.html",inf=(randint(43,52)))
        elif 50 < admission_prob < 60:
            return render_template("Engg-mmgt_show.html",inf=(randint(53,62)))
        elif 60 < admission_prob < 70:
            return render_template("Engg-mmgt_show.html",inf=(randint(63,72)))
        elif 70 < admission_prob < 80:
            return render_template("Engg-mmgt_show.html",inf=(randint(73,82)))
        elif 80 < admission_prob < 95:
            return render_template("Engg-mmgt_show.html",inf=(randint(83,92)))
        elif 95 < admission_prob < 100:
            return render_template("Engg-mmgt_show.html",inf=(randint(93,97)))
    return render_template("Engg-mmgt_index.html")
    #return 'Hello, World!' + str(infprob)

@app.route("/univlist_engg_mmgt")
def univlist_engg_mmgt():
    return render_template('Engg_mmgt_Univ.html')

'''----------------------IT----------------------------'''

@app.route('/IT', methods=["GET","POST"])
def IT():
    if request.method=="POST":
        myDict=request.form
        Aggregate=float(myDict['Aggregate'])
        GRE=int(myDict['GRE'])
        Internship=int(myDict['Internship'])
        Germanlevel=int(myDict['Germanlevel'])
        Private=int(myDict['Private'])
        Project=int(myDict['Project'])

        
        inputFeatures=[[Aggregate,GRE,Internship,Germanlevel,Private,Project]]
        admission_prob=model6.predict_proba(inputFeatures)[:,1]
        admission_prob=admission_prob*100
        print(admission_prob)
        if admission_prob < 10:
            return render_template("IT_show.html",inf=(randint(10,17)))
        elif 10 < admission_prob < 20:
            return render_template("IT_show.html",inf=(randint(18,27)))
        elif 20 < admission_prob < 30:
            return render_template("IT_show.html",inf=(randint(28,37)))
        elif 30 < admission_prob < 40:
            return render_template("IT_show.html",inf=(randint(38,47)))
        elif 40 < admission_prob < 50:
            return render_template("IT_show.html",inf=(randint(48,57)))
        elif 50 < admission_prob < 60:
            return render_template("IT_show.html",inf=(randint(58,67)))
        elif 60 < admission_prob < 70:
            return render_template("IT_show.html",inf=(randint(68,77)))
        elif 70 < admission_prob < 80:
            return render_template("IT_show.html",inf=(randint(78,87)))
        elif 80 < admission_prob < 95:
            return render_template("IT_show.html",inf=(randint(88,94)))
        elif 95 < admission_prob < 100:
            return render_template("IT_show.html",inf=(randint(95,98)))
            
    return render_template("IT_index.html")
    
@app.route("/univlist_IT")
def univlist_IT():
    return render_template('IT_univ.html')

'''----------------------Management----------------------------'''

@app.route('/Management', methods=["GET","POST"])
def Management():
    if request.method=="POST":
        myDict=request.form
        Aggregate=float(myDict['Aggregate'])
        WorkExperienceless1=int(myDict['WorkExperienceless1'])
        Private=int(myDict['Private'])
        WorkExperienceMore1=int(myDict['WorkExperienceMore1'])
        GRE=int(myDict['GRE'])
        Germanlevel=int(myDict['Germanlevel'])
        

        
        inputFeatures=[[Aggregate,WorkExperienceless1,Private,WorkExperienceMore1,GRE,Germanlevel]]
        admission_prob=model7.predict_proba(inputFeatures)[:,1]
        admission_prob=admission_prob*100
        print(admission_prob)
        if admission_prob < 10:
            return render_template("Management_show.html",inf=(randint(9,15)))
        elif 10 < admission_prob < 20:
            return render_template("Management_show.html",inf=(randint(15,22)))
        elif 20 < admission_prob < 30:
            return render_template("Management_show.html",inf=(randint(23,32)))
        elif 30 < admission_prob < 40:
            return render_template("Management_show.html",inf=(randint(33,42)))
        elif 40 < admission_prob < 50:
            return render_template("Management_show.html",inf=(randint(43,52)))
        elif 50 < admission_prob < 60:
            return render_template("Management_show.html",inf=(randint(53,62)))
        elif 60 < admission_prob < 70:
            return render_template("Management_show.html",inf=(randint(63,72)))
        elif 70 < admission_prob < 80:
            return render_template("Management_show.html",inf=(randint(73,82)))
        elif 80 < admission_prob < 95:
            return render_template("Management_show.html",inf=(randint(83,92)))
        elif 95 < admission_prob < 100:
            return render_template("Management_show.html",inf=(randint(93,98)))
    return render_template("Management_index.html")

@app.route("/univlist_management")
def univlist_management():
    return render_template('Management_univ.html')

'''----------------------Materials----------------------------'''


@app.route('/Materials', methods=["GET","POST"])
def Materials():
    if request.method=="POST":
        myDict=request.form
        Aggregate=float(myDict['Aggregate'])
        DegreeCompleted=int(myDict['DegreeCompleted'])
        Internship=int(myDict['Internship'])
        Germanlevel=int(myDict['Germanlevel'])
        GRE=int(myDict['GRE'])
        Winter=int(myDict['Winter'])

        
        inputFeatures=[[Aggregate,DegreeCompleted,Internship,Germanlevel,GRE,Winter]]
        admission_prob=model8.predict_proba(inputFeatures)[:,1]
        admission_prob=admission_prob*100
        print(admission_prob)
        if admission_prob < 10:
            return render_template("Material_show.html",inf=(randint(10,15)))
        elif 10 < admission_prob < 20:
            return render_template("Material_show.html",inf=(randint(16,25)))
        elif 20 < admission_prob < 30:
            return render_template("Material_show.html",inf=(randint(26,34)))
        elif 30 < admission_prob < 40:
            return render_template("Material_show.html",inf=(randint(35,44)))
        elif 40 < admission_prob < 50:
            return render_template("Material_show.html",inf=(randint(45,54)))
        elif 50 < admission_prob < 60:
            return render_template("Material_show.html",inf=(randint(55,64)))
        elif 60 < admission_prob < 70:
            return render_template("Material_show.html",inf=(randint(65,74)))
        elif 70 < admission_prob < 80:
            return render_template("Material_show.html",inf=(randint(75,84)))
        elif 80 < admission_prob < 90:
            return render_template("Material_show.html",inf=(randint(85,90)))
        elif 90 < admission_prob < 100:
            return render_template("Material_show.html",inf=(randint(91,96)))
            
    return render_template("Material_index.html")
    
@app.route("/univlist_materials")
def univlist_materials():
    return render_template('Materials_univ.html')

'''----------------------Mechanical----------------------------'''

@app.route('/Mechanical', methods=["GET","POST"])
def Mechanical():
    if request.method=="POST":
        myDict=request.form
        Aggregate=float(myDict['Aggregate'])
        GRE=int(myDict['GRE'])
        Internship=int(myDict['Internship'])
        DegCompleted=int(myDict['DegCompleted'])
        Winter=int(myDict['Winter'])
        GermanLevel=int(myDict['GermanLevel'])

        
        inputFeatures=[[Aggregate,GRE,Internship,DegCompleted,Winter,GermanLevel]]
        admission_prob=model10.predict_proba(inputFeatures)[:,1]
        admission_prob=admission_prob*100
        print(admission_prob)
        if admission_prob < 10:
            return render_template("Mechanical_show.html",inf=(randint(10,15)))
        elif 10 < admission_prob < 20:
            return render_template("Mechanical_show.html",inf=(randint(16,25)))
        elif 20 < admission_prob < 30:
            return render_template("Mechanical_show.html",inf=(randint(26,34)))
        elif 30 < admission_prob < 40:
            return render_template("Mechanical_show.html",inf=(randint(35,44)))
        elif 40 < admission_prob < 50:
            return render_template("Mechanical_show.html",inf=(randint(45,54)))
        elif 50 < admission_prob < 60:
            return render_template("Mechanical_show.html",inf=(randint(55,64)))
        elif 60 < admission_prob < 70:
            return render_template("Mechanical_show.html",inf=(randint(65,74)))
        elif 70 < admission_prob < 80:
            return render_template("Mechanical_show.html",inf=(randint(75,84)))
        elif 80 < admission_prob < 90:
            return render_template("Mechanical_show.html",inf=(randint(85,90)))
        elif 90 < admission_prob < 100:
            return render_template("Mechanical_show.html",inf=(randint(91,96)))
            
    return render_template("Mechanical_index.html")

@app.route("/univlist_mechanical")
def univlist_mechanical():
    return render_template('Mechanical_univ.html')

'''----------------------Mechatronics----------------------------'''

@app.route('/Mechatronics', methods=["GET","POST"])
def Mechatronics():
    if request.method=="POST":
        myDict=request.form
        Aggregate=float(myDict['Aggregate'])
        GRE=int(myDict['GRE'])
        Internship=int(myDict['Internship'])
        Germanlevel=int(myDict['Germanlevel'])
        DegreeCompleted=int(myDict['DegreeCompleted'])
        Project=int(myDict['Project'])

        
        inputFeatures=[[Aggregate,GRE,Internship,Germanlevel,DegreeCompleted,Project]]
        admission_prob=model9.predict_proba(inputFeatures)[:,1]
        admission_prob=admission_prob*100
        print(admission_prob)
        if admission_prob < 10:
            return render_template("Mechatronics_show.html",inf=(randint(10,17)))
        elif 10 < admission_prob < 20:
            return render_template("Mechatronics_show.html",inf=(randint(18,27)))
        elif 20 < admission_prob < 30:
            return render_template("Mechatronics_show.html",inf=(randint(28,37)))
        elif 30 < admission_prob < 40:
            return render_template("Mechatronics_show.html",inf=(randint(38,47)))
        elif 40 < admission_prob < 50:
            return render_template("Mechatronics_show.html",inf=(randint(48,57)))
        elif 50 < admission_prob < 60:
            return render_template("Mechatronics_show.html",inf=(randint(58,67)))
        elif 60 < admission_prob < 70:
            return render_template("Mechatronics_show.html",inf=(randint(68,77)))
        elif 70 < admission_prob < 80:
            return render_template("Mechatronics_show.html",inf=(randint(78,87)))
        elif 80 < admission_prob < 95:
            return render_template("Mechatronics_show.html",inf=(randint(88,94)))
        elif 95 < admission_prob < 100:
            return render_template("Mechatronics_show.html",inf=(randint(95,98)))
            
    return render_template("Mechatronics_index.html")
    
@app.route("/univlist_mechatronics")
def univlist_mechatronics():
    return render_template('Mechatronics_univ.html')

@app.route("/contact", methods = ['GET', 'POST']) # make the web page connect to our respective class. 
def contact():
    return render_template('contact.html')


if __name__ == "__main__": 
    app.run(debug=True)



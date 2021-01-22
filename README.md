# End-to-End Data Science project: Student profile evaluation for Higher Education in Germany!!
* Created a website where students can find all necessary information for higher education in Germany.
* Website created has been deployed with machine learning models running in the backend. Each course that a student wants to pursue has its own Machine learning model and a web interface link which is been attached to home webpage. On the link related to the particular subject the student can find a **"Profile evaluation form"**, all the student has to do is fill in his/her details and click **Submit**. Once the request has been submitted the Machine Learning model running in the backend will evaluate the profile and give the probability of the student getting an admission in German university. The probability can be between 0-100%. 
* After evaluation the student can click on **_Get university list_** tab and get the university list related to that course. 

## Code and Resources Used
 - **Python Version:** 3.7  
 - **Packages:** pandas, numpy, Flask, pickle, Scikit learn
 - **Web Programming language**: HTML, Jinja templating
 - **Web application deployment**: Heroku

## Dataset for training the Models
* The model for each subject are trained on atleast **ten thousand datasets**. This data has been collected from various websites like facebook, DAAD and the website of some higher education consulting companies. After all web scraping and manually looking for data the data still was not enough for the model to train on. Then I created my own dataset, I used by expertise to build a strategically strong data which would resemble the real world data. I built such dataset for each subject field.

## Key points of the project

* Used machine learning to build predictors for each subject field. After trying with different models the accuracy of these models were the highest
  - **Logistic Regression: 90% accuracy.**
  - **A 2 layer Deep neural network: 91% accuracy.**
  - **Logistic Regression with best parameters using RandomizedSearchCV: 96% accuracy**.
* Each model has been seperately deployed on the cloud and the link of each model is attached to the User Interface of this project. Used Flask framework to deploy the models into production.
* Used Bootstrap Html & CSS templates for web development/design. Used Jinja templating to add dynamic expert comments after student profile evaluation. 
* Deployed the web application on Heroku cloud service platform. 

## Output
Use this link to see the project's final output: https://higher-education-germany-vikas.herokuapp.com/

## Conclusion
I created this project to make student's life simple as the students can directly go to the website find accurate information on German education, get their profile evaluated and finally get a university list based on the prediction. 



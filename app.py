from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import joblib
import matplotlib
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = joblib.load('HRanalysis.pkl')
@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        Age = (float)(request.form['Age'])
        DailyRate = int(request.form['DailyRate'])
        DistanceFromHome = int(request.form['DistanceFromHome'])
        Education = int(request.form['Education'])
        EnvironmentSatisfaction = int(request.form['EnvironmentSatisfaction'])
        HourlyRate = int(request.form['HourlyRate'])
        JobInvolvement = int(request.form['JobInvolvement'])
        JobLevel = int(request.form['JobLevel'])
        JobSatisfaction = int(request.form['JobSatisfaction'])
        MonthlyIncome = int(request.form['MonthlyIncome'])
        MonthlyRate = int(request.form['MonthlyRate'])
        NumCompaniesWorked = int(request.form['NumCompaniesWorked'])
        PercentSalaryHike = int(request.form['PercentSalaryHike'])
        PerformanceRating = int(request.form['PerformanceRating'])
        RelationshipSatisfaction = int(request.form['RelationshipSatisfaction'])
        StockOptionLevel = int(request.form['StockOptionLevel'])
        TotalWorkingYears = int(request.form['TotalWorkingYears'])
        TrainingTimesLastYear = int(request.form['TrainingTimesLastYear'])
        WorkLifeBalance = int(request.form['WorkLifeBalance'])
        YearsAtCompany = int(request.form['YearsAtCompany'])
        YearsInCurrentRole = int(request.form['YearsInCurrentRole'])
        YearsSinceLastPromotion = int(request.form['YearsSinceLastPromotion'])
        YearsWithCurrManager = int(request.form['YearsWithCurrManager'])
        Attrition = int(request.form['Attrition'])
        BusinessTravel = int(request.form['BusinessTravel'])
        Department = int(request.form['Department'])
        EducationField = int(request.form['EducationField'])
        Gender = int(request.form['Gender'])
        JobRole = int(request.form['JobRole'])
        MaritalStatus = int(request.form['MaritalStatus'])
        OverTime = int(request.form['OverTime'])

        prediction = model.predict([[Age, DailyRate, DistanceFromHome, Education, EnvironmentSatisfaction, HourlyRate, 
        JobInvolvement, JobLevel, JobSatisfaction, MonthlyIncome, MonthlyRate, NumCompaniesWorked, PercentSalaryHike, 
        PerformanceRating, RelationshipSatisfaction, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, 
        YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager, BusinessTravel, Department, EducationField, Gender, JobRole, MaritalStatus, OverTime]])

        if prediction==1:
             return render_template('index.html',prediction_text="YOU ARE CULTURALLY FIT FOR OUR COMPANY")
        else:
             return render_template('index.html',prediction_text="YOU ARE NOT CULTURALLY FIT FOR OUR COMPANY")
                
if __name__=="__main__":
    app.run(debug=True)

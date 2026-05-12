import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "age": [45, 52, 39, 60, 48, 55, 62, 41, 58, 50, 67, 44],
    "gender": ["Male", "Female", "Male", "Female", "Male", "Male", "Female", "Female", "Male", "Female", "Male", "Female"],
    "blood_pressure": [130, 145, 120, 160, 135, 150, 170, 125, 155, 140, 165, 128],
    "cholesterol": [220, 250, 180, 280, 230, 260, 300, 190, 270, 240, 310, 200],
    "diabetes": ["No", "Yes", "No", "Yes", "No", "Yes", "Yes", "No", "Yes", "No", "Yes", "No"],
    "heart_disease": ["No", "Yes", "No", "Yes", "No", "Yes", "Yes", "No", "Yes", "No", "Yes", "No"]
}

dataframe = pd.DataFrame(data)

print("Health dataset : ")
print(dataframe)

print("\nDataset Information : ")
print(dataframe.info())

#check missing data 

print("\nMissing Values : ")
print(dataframe.isnull().sum())

print("\nAverage value by Heart Disease : ")
print(dataframe.groupby("heart_disease")[["age","blood_pressure","cholesterol"]].mean())

print("\nCorrelation : ")
print(dataframe[["age","blood_pressure","cholesterol"]].corr())

sns.countplot(data = dataframe, x = "heart_disease")
plt.title("Heart Disease Count")
plt.xlabel("Heart Disease")
plt.ylabel("Patient Count")
plt.show()

sns.barplot(data=dataframe, x="heart_disease", y="cholesterol",)
plt.title("Average Cholesterol by Heart Disease")
plt.xlabel("Heart Disease")
plt.ylabel("Cholesterol")
plt.show()

sns.scatterplot(data=dataframe, x="age", y="blood_pressure", hue="heart_disease")
plt.title("Age vs Blood Pressure")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.show()

sns.heatmap(dataframe[["age", "blood_pressure", "cholesterol"]].corr(), annot=True)
plt.title("Health Risk Correlation")
plt.show()
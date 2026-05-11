import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


#creating sample data
data = {
    "tenure": [1, 5, 12, 24, 2, 36, 8, 48, 3, 60],
    "monthly_charges": [80, 70, 65, 55, 90, 50, 75, 45, 85, 40],
    "support_calls": [5, 3, 2, 1, 6, 0, 4, 1, 5, 0],
    "contract_type": [
        "monthly", "monthly", "yearly", "yearly", "monthly",
        "yearly", "monthly", "yearly", "monthly", "yearly"
    ],
    "churn": [
        "yes", "yes", "no", "no", "yes",
        "no", "yes", "no", "yes", "no"
    ]
}

dataframe = pd.DataFrame(data)

dataframe["contract_type"] = dataframe["contract_type"].map({
    "monthly": 0,
    "yearly": 1
})

dataframe["churn"] = dataframe["churn"].map({
    "yes": 1,
    "no": 0
})

x = dataframe [["tenure","monthly_charges","support_calls","contract_type"]]
y = dataframe ["churn"]

x_train, x_test, y_train, y_test = train_test_split(
    x,y, test_size=0.3, random_state=10
)

model = LogisticRegression()
model.fit(x_train, y_train)

prediction = model.predict(x_test)

print("Accuracy : ")
print(accuracy_score(y_test,prediction))

print("\n Confusion Matrix : ")
print(confusion_matrix(y_test,prediction))

print("\n Classification Report : ")
print(classification_report(y_test,prediction))

#adding a new customer to predict information of

new_customer = pd.DataFrame({
    "tenure": [4],
    "monthly_charges": [85],
    "support_calls": [4],
    "contract_type": [0]
})

result = model.predict(new_customer)

if result[0] == 1:
    print("New Customer Prediction : May Churn")
else:
    print("New Customer Prediction : May Stay")
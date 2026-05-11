import pandas as pd
import matplotlib.pyplot as plt

data = {
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
    "sales": [12000, 15000, 18000, 14000, 22000, 25000, 21000, 28000],
    "expenses": [7000, 8000, 9000, 8500, 11000, 12000, 10000, 13000],
    "promotion": ["No", "No", "Yes", "No", "Yes", "Yes", "No", "Yes"]
}

dataframe = pd.DataFrame(data)

dataframe["profit"] = dataframe ["sales"] - dataframe ["expenses"]

promotional_sales = dataframe.groupby("promotion")["sales"].mean()

print("sales Data")
print(dataframe)

print("\nTotal sales:")
print(dataframe["sales"].sum())

print("\nAverage sales")
print(dataframe["sales"].mean())

print("\nHighest sales month")
print(dataframe.loc[dataframe["sales"].idxmax()])

print("\nLowest sales month")
print(dataframe.loc[dataframe["sales"].idxmin()])

print("\nAverage sales without Promotion")
print(promotional_sales)

plt.plot(dataframe["month"], dataframe["sales"], marker="o")
plt.title("monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

plt.bar(dataframe["month"], dataframe["profit"])
plt.title("monthly profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

plt.bar(promotional_sales.index, promotional_sales.values)
plt.title("Average Sales : Promotion vs No Promotion")
plt.xlabel("Promotion")
plt.ylabel("Average Sales")
plt.show()
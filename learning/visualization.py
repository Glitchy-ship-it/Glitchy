import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as mtpt



# Months = ["Jan","Feb","Mar","April","May","June"]
# Sales = [1000,200,500,700,800,1500]

# mtpt.xlabel("Months")
# mtpt.ylabel("Sales")
# mtpt.title(f"Graph of Monthly Sales for the Months : {Months}")
# mtpt.plot(Months,Sales,marker="*",color="Red")
# mtpt.show()
# mtpt.savefig("Sales_Chart.png")

data = sns.load_dataset('iris')
# print(data.describe())

# sns.pairplot(data=data,hue="species",palette="dark")
# mtpt.title("")
# mtpt.show()

# sns.boxplot(data=data,x="species",y="petal_length")
# mtpt.show()

mtpt.pie(x="species", np.float32)
mtpt.show()
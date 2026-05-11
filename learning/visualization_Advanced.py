import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as mtpt


data = sns.load_dataset("penguins")
# print(data.isnull().sum())
# corrl = data.corr(numeric_only=True)
# sns.heatmap(corrl,annot=True,cmap="coolwarm",linewidths=0.5)
sns.barplot(data=data, x="sex", y="bill_depth_mm")
mtpt.show()

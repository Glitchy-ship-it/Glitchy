import pandas as pd
import numpy as np
import seaborn as sns
np.random.seed(10)

# Data = {
#     "Product": ["Laptop", "Phone", "Desktop","Dragon Dildo"],
#     "Price" : [50000,10000,70000,100000],
#     "Stock" : [10, 50, 60, 1]
# }

data = sns.load_dataset("tips")

print(data.head())
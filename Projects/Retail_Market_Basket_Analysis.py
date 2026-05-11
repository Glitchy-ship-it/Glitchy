import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

transactions = [
    ["milk", "bread", "Butter"],
    ["bread", "Butter", "jam"],
    ["milk", "bread"],
    ["milk", "bread", "Butter", "eggs"],
    ["bread", "eggs"],
    ["milk", "Butter"],
    ["milk", "bread", "Butter"],
    ["bread", "jam"],
    ["milk", "bread", "jam"],
    ["Butter", "jam"],
    ["milk", "eggs", "bread"],
    ["bread", "Butter", "eggs"],
    ["milk", "bread", "Butter", "jam"],
    ["eggs", "bread"],
    ["milk", "Butter", "jam"]
]

clean_transaction = []

for basket in transactions:
    clean_basket = list(set(basket))
    clean_transaction.append(clean_basket)

all_products = []

for basket in clean_transaction:
    for product in basket:
        all_products.append(product)

product_count = pd.Series(all_products).value_counts()

print("Top Selling PRODUCTS")
print(product_count)

plt.bar(product_count.index, product_count.values)
plt.title("Most Frequently Bought Products")
plt.xlabel("Products")
plt.ylabel("Purchase Count")
plt.show()

te = TransactionEncoder()

te_array = te.fit(clean_transaction).transform(clean_transaction)

dataframe = pd.DataFrame(te_array,columns=te.columns_)

frequent_items = apriori(dataframe,min_support=0.25,use_colnames=True)

rules = association_rules(
    frequent_items,
    metric="confidence",
    min_threshold=0.6
)

rules = rules.sort_values(by="lift", ascending=False)

print("\nTransactions")
print(dataframe)

print("\nFrequent Items")
print(frequent_items)

print("\nAssociation Rules")
print(rules[["antecedents", "consequents", "support", "confidence", "lift"]])

strong_rules = rules[
    (rules["confidence"] >= 0.7) &
    (rules["lift"] > 1)
]

print("\nStrong Business Rules:")
print(strong_rules[["antecedents", "consequents", "support", "confidence", "lift"]])

print("\nRecommendations:")

for index, row in strong_rules.iterrows():
    antecedent = list(row["antecedents"])
    consequent = list(row["consequents"])

    print(f"If customers buy {antecedent}, recommend {consequent}.")
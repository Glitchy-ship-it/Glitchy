import numpy as np

np.random.seed(10)

products = ["toothpaste", "detergent", "face wash","lotion","soap","oil", "bread"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday"]

sales = np.random.randint(10,200,size=len(products))

# print("Sales Matrix (rows = days, columns = products):\n", sales)

# total_sales_day = np.sum(sales, axis=1)
# # print("Total Sales Per day = ", total_sales_day)

# total_product_sales = np.sum(sales, axis=0)
# print("\nTotal Sales per Product:")
# for a, products in enumerate(products):
#     print(f"{products}: {total_product_sales[a]} units")

# for a, products in enumerate(products):
#     print(a, " ", products)

# best_selling = np.argmax(total_product_sales)

# print("\nTotal Sales per Product:")
# for a, products in enumerate(products):
#     print(f"{products}: {total_product_sales[a]} units")

# print(f"Best selling Product : {products[best_selling]}")

customers = np.random.normal(4.3,0.3,100)

# print(f"Average Rating : {customers.mean():.2f} \n" f"Standard rating : {customers.std():.2f}")

price = np.random.randint(50,200, size=len(products))

# print("Products along with Prices :")
# for i, products in enumerate(products):
#     print(f"{products} : {price[i]}")

revenue = price*sales

for i, products in enumerate(products):
    print(f"{products} : {revenue[i]}")


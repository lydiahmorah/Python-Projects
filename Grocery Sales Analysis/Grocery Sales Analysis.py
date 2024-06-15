
#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading the dataset
df_products=pd.read_csv("Clean Grocery Store Sales.csv")
df_products.head(10)

#Calculating the total_sales column
df_products['total_sales'] = df_products['price'] * df_products['average_units_sold']
df_products

## Visualising Total Sales by Product Type
plt.figure(figsize=(10, 7))
plt.bar(df_products['product_type'], df_products['total_sales'], color='blue')
plt.xlabel('Product Type')
plt.ylabel('Total Sales')
plt.title('Total Sales by Product Type')
plt.show()
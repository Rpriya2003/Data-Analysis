import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")  

sales_summary = df.groupby("Product")["Sales"].sum()
print(sales_summary)

sales_summary.plot(kind="bar", title="Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

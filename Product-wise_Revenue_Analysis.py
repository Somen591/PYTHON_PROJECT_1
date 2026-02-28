import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

products = ['Mobile', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch']
revenue = [450000, 720000, 280000, 150000, 320000]

# Step 1: NumPy
revenue_np = np.array(revenue)

print("Total revenue:", np.sum(revenue_np))
print("Average revenue:", np.mean(revenue_np))
print("Highest revenue:", np.max(revenue_np))
print("Lowest revenue:", np.min(revenue_np))

top_product = products[np.argmax(revenue_np)]
print("Top earning product:", top_product)

# Step 2: Pandas
df = pd.DataFrame({
    "Product": products,
    "Revenue": revenue
})

df_sorted = df.sort_values(by="Revenue", ascending=False)
total_revenue = df["Revenue"].sum()
df["Contribution (%)"] = (df["Revenue"] / total_revenue) * 100

print("\nSorted Revenue Data:")
print(df_sorted)

# Step 3: Insights
print("\nBusiness Insights:")
print("1. Laptop generates the highest revenue among all products.")
print("2. Headphones have the lowest revenue contribution.")
print("3. Marketing and bundling strategies can improve low-performing product sales.")

# Step 4: Visualization
plt.bar(df["Product"], df["Revenue"], color='skyblue', label="Sales 2025")
plt.title("Product-wise Revenue (2025)")
plt.xlabel("Products")
plt.ylabel("Revenue")
plt.xticks(rotation=30)
plt.grid(axis='y')
plt.legend()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read Excel data
df = pd.read_excel("sales_data.xlsx", header=1)

# Step 2: Remove empty columns
df = df.loc[:, ~df.columns.astype(str).str.contains("^Unnamed")]

# Step 3: Calculate total sales
df["Total Sales"] = df["Quantity"] * df["Price"]

# Step 4: Group sales by product
product_sales = df.groupby("Product")["Total Sales"].sum()

# Step 5: Create bar chart
plt.figure(figsize=(10, 6))

bars = plt.bar(
    product_sales.index,
    product_sales.values,
    color="steelblue"
)

# Step 6: Add graph title and labels
plt.title("Product Wise Sales Report", fontsize=16)
plt.xlabel("Product Name", fontsize=12)
plt.ylabel("Total Sales (Rs.)", fontsize=12)

# Step 7: Display values above bars
for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"Rs. {height:,.0f}",
        ha="center",
        va="bottom"
    )

# Step 8: Improve graph appearance
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()

# Step 9: Save graph as image
plt.savefig("sales_graph.png", dpi=300)

# Step 10: Display graph
plt.show()

print("Sales graph generated successfully!")

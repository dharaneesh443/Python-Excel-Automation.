
import pandas as pd

# Step 1: Read Excel file
df = pd.read_excel("sales_data.xlsx",header=1)

# Step 2: Display original data
print("ORIGINAL SALES DATA")
print(df)

# Step 3: Calculate total sales
df["Total Sales"] = df["Quantity"] * df["Price"]

# Step 4: Calculate total quantity
total_quantity = df["Quantity"].sum()

# Step 5: Calculate total revenue
total_revenue = df["Total Sales"].sum()

# Step 6: Find highest selling product by revenue
highest_sale = df.loc[df["Total Sales"].idxmax()]

# Step 7: Create summary report
summary = pd.DataFrame({
    "Description": [
        "Total Quantity Sold",
        "Total Revenue",
        "Highest Revenue Transaction"
    ],
    "Value": [
        total_quantity,
        total_revenue,
        highest_sale["Product"]
    ]
})

# Step 8: Save output in a new Excel file
with pd.ExcelWriter("sales_report.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Sales Details", index=False)
    summary.to_excel(writer, sheet_name="Summary", index=False)

print("\nREPORT GENERATED SUCCESSFULLY!")
print("Total Quantity:", total_quantity)
print("Total Revenue:", total_revenue)
print("Highest Revenue Product:", highest_sale["Product"])

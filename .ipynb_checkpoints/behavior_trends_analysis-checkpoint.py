import pandas as pd
def import_data(file_path):
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
        return df
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)
        return df
    else:
        return "Unsupported file type"

file_path = "Customer_Behavior.xlsx"
df = import_data(file_path)
print(df.columns)
print(df.head())

# def filter_data(df):
#     df = df[df["CustomerID"].notna()]
#     df = df[(df["Quantity"] >= 0) & (df["UnitPrice"] >= 0)]
#     return df

# filtered_df = filter_data(df)
# print(filtered_df.head())


# def loyalty_customers(df, min_purchases):
#     purchase_counts = df.groupby("CustomerID").size().reset_index(name='PurchaseCount')
#     loyal_customers = purchase_counts[purchase_counts['PurchaseCount'] >= min_purchases]
#     return loyal_customers

# min_purchases = 10 
# loyal_df = loyalty_customers(df, min_purchases)
# print(loyal_df.head())

# def quarterly_revenue(df):
#     df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
#     df['Quarter'] = df['InvoiceDate'].dt.to_period('Q')
#     df['Revenue'] = df['Quantity'] * df['UnitPrice']
#     total_revenue = df.groupby('Quarter')['Revenue'].sum().reset_index()
#     total_revenue.columns = ['Quarter', 'Total Revenue']
#     return total_revenue

# revenue_df = quarterly_revenue(df)
# print(revenue_df.head())
  

def high_demand_products(df):
    total_quantity = df.groupby('StockCode')['Quantity'].sum().reset_index()
    sorted_products = total_quantity.sort_values(by='Quantity', ascending=False)
    top_products = sorted_products.head(top_n)
    return top_products

top_n = 10 
top_products_df = high_demand_products(df, top_n)
print(top_products_df)





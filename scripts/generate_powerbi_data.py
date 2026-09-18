import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

np.random.seed(101)
random.seed(101)

NUM_RECORDS = 10000
START_DATE = datetime(2022, 1, 1)
END_DATE = datetime(2024, 12, 31)

# --- 1. REFERENCE DATA ---
categories_products = {
    'Electronics': [('Laptop', 45000, 38000), ('Smartphone', 25000, 20000), ('Tablet', 18000, 14000), ('Monitor', 12000, 8000)],
    'Furniture': [('Office Chair', 6000, 3500), ('Desk', 9000, 5500), ('Sofa', 28000, 18000)],
    'Clothing': [('T-Shirt', 600, 250), ('Jeans', 1800, 800), ('Shoes', 2500, 1200)],
    'Home Appliances': [('Washing Machine', 32000, 24000), ('Refrigerator', 38000, 28000)],
    'Accessories': [('Smart Watch', 4000, 2000), ('Backpack', 1500, 700), ('Headphones', 2800, 1400), ('Mouse', 600, 250), ('Keyboard', 900, 400)]
}

products_list = []
prod_id = 1
for cat, items in categories_products.items():
    for name, price, cost in items:
        products_list.append({
            'Product_ID': f"PRD-{prod_id:04d}",
            'Product': name,
            'Category': cat,
            'Sub_Category': name,
            'Price': price,
            'Cost': cost
        })
        prod_id += 1

locations = {
    'South': {'Tamil Nadu': ['Chennai', 'Coimbatore'], 'Karnataka': ['Bengaluru', 'Mysuru'], 'Kerala': ['Kochi', 'Trivandrum'], 'Telangana': ['Hyderabad']},
    'North': {'Delhi': ['New Delhi'], 'Punjab': ['Chandigarh', 'Ludhiana'], 'Haryana': ['Gurugram']},
    'West': {'Maharashtra': ['Mumbai', 'Pune', 'Nagpur'], 'Gujarat': ['Ahmedabad', 'Surat']},
    'East': {'West Bengal': ['Kolkata', 'Darjeeling'], 'Odisha': ['Bhubaneswar']},
    'Central': {'Madhya Pradesh': ['Bhopal', 'Indore']}
}

loc_list = [{'Region': r, 'State': s, 'City': c} for r, states in locations.items() for s, cities in states.items() for c in cities]
customer_segments = ['Consumer', 'Corporate', 'Small Business']
genders = ['Male', 'Female', 'Other']
payment_modes = ['UPI', 'Credit Card', 'Debit Card', 'Net Banking', 'Cash on Delivery', 'Wallet']
order_statuses = ['Completed', 'Completed', 'Completed', 'Completed', 'Cancelled', 'Returned', 'Pending']

customers = []
for i in range(1, 401):
    customers.append({
        'Customer_ID': f"CUS-{i:04d}",
        'Customer_Name': f"Customer {i}",
        'Customer_Age': random.randint(18, 75),
        'Gender': random.choice(genders),
        'Customer_Segment': random.choice(customer_segments)
    })

# --- 2. GENERATE BASE DATA ---
data = []
for i in range(NUM_RECORDS):
    cust = random.choice(customers)
    prod = random.choice(products_list)
    loc = random.choice(loc_list)
    
    order_date = START_DATE + timedelta(days=random.randint(0, (END_DATE - START_DATE).days))
    
    quantity = random.randint(1, 6)
    unit_price = prod['Price'] * random.uniform(0.95, 1.05)
    cost = prod['Cost'] * random.uniform(0.95, 1.05)
    
    discount_pct = random.choice([0, 0, 0.05, 0.10, 0.15, 0.20])
    gross_sales = quantity * unit_price
    discount_amount = gross_sales * discount_pct
    net_sales = gross_sales - discount_amount
    total_cost = quantity * cost
    profit = net_sales - total_cost
    
    data.append({
        'Order_ID': f"ORD-{20220000 + i}",
        'Order_Date': order_date.strftime('%Y-%m-%d'),
        'Customer_ID': cust['Customer_ID'],
        'Customer_Name': cust['Customer_Name'],
        'Customer_Age': cust['Customer_Age'],
        'Gender': cust['Gender'],
        'Customer_Segment': cust['Customer_Segment'],
        'Product_ID': prod['Product_ID'],
        'Product': prod['Product'],
        'Category': prod['Category'],
        'Sub_Category': prod['Sub_Category'],
        'Region': loc['Region'],
        'State': loc['State'],
        'City': loc['City'],
        'Quantity': quantity,
        'Unit_Price': round(unit_price, 2),
        'Discount': discount_pct,
        'Sales': round(net_sales, 2),
        'Cost': round(total_cost, 2),
        'Profit': round(profit, 2),
        'Payment_Mode': random.choice(payment_modes),
        'Order_Status': random.choice(order_statuses)
    })

df = pd.DataFrame(data)

# --- 3. INJECT DATA QUALITY ISSUES (For Power Query Practice) ---
# 1. Missing values
df.loc[df.sample(frac=0.015).index, 'Customer_Age'] = np.nan
df.loc[df.sample(frac=0.01).index, 'City'] = np.nan

# 2. Duplicate rows (append 35 duplicate rows)
duplicates = df.sample(n=35)
df = pd.concat([df, duplicates], ignore_index=True)

# 3. Inconsistent text casing
sample_idx = df.sample(frac=0.02).index
df.loc[sample_idx, 'Category'] = df.loc[sample_idx, 'Category'].str.lower()
df.loc[df.sample(frac=0.01).index, 'Category'] = df['Category'].str.upper()

# 4. Extra spaces
df.loc[df.sample(frac=0.02).index, 'Customer_Name'] = df['Customer_Name'] + "   "
df.loc[df.sample(frac=0.02).index, 'Product'] = "  " + df['Product']

# 5. Incorrect data types / Invalid values
# Put some text into the numeric Discount column
df['Discount'] = df['Discount'].astype(object)
df.loc[df.sample(n=5).index, 'Discount'] = "Ten Percent"
df.loc[df.sample(n=5).index, 'Discount'] = "N/A"
# Invalid order dates
df.loc[df.sample(n=8).index, 'Order_Date'] = "1900-01-01"

# --- 4. EXPORT TO CSV ---
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.abspath(os.path.join(script_dir, "..", "data", "ecommerce_sales_raw.csv"))
df.to_csv(output_path, index=False)
print(f"Data generation complete. Saved {len(df)} rows to {output_path}")

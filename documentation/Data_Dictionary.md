# Data Dictionary

This document explains the columns used in the `ecommerce_sales_raw.csv` dataset and the resulting Star Schema.

## FactSales (Fact Table)
* `Order_ID`: Unique identifier for each transaction.
* `Order_Date`: Date the order was placed.
* `Customer_ID`: Foreign Key linking to DimCustomer.
* `Product_ID`: Foreign Key linking to DimProduct.
* `Quantity`: Number of units purchased in the transaction.
* `Unit_Price`: Price per unit before discount.
* `Discount`: Discount percentage applied to the gross sales (e.g., 0.10 for 10%).
* `Sales`: Net revenue generated after applying the discount.
* `Cost`: Total cost to the business for the units sold.
* `Profit`: Net Sales minus Total Cost.
* `Order_Status`: Status of the order (Completed, Pending, Cancelled, Returned).

## DimCustomer (Dimension Table)
* `Customer_ID`: Primary Key.
* `Customer_Name`: Full name of the customer.
* `Customer_Age`: Age of the customer.
* `Gender`: Gender of the customer.
* `Customer_Segment`: Classification of the buyer (Consumer, Corporate, Small Business).

## DimProduct (Dimension Table)
* `Product_ID`: Primary Key.
* `Product`: Name of the specific item sold.
* `Category`: Broad classification (e.g., Electronics, Furniture).
* `Sub_Category`: Granular classification.

## DimDate (Dimension Table)
* Automatically generated using DAX to support Time-Intelligence calculations (YTD, YoY).

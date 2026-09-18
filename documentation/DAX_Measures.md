# DAX Measures Reference Guide

This document stores the Data Analysis Expressions (DAX) used in the Power BI dashboard.

## Core KPIs
```dax
Total Sales = SUM(FactSales[Sales])
Total Profit = SUM(FactSales[Profit])
Total Orders = DISTINCTCOUNT(FactSales[Order_ID])
Total Customers = DISTINCTCOUNT(FactSales[Customer_ID])
Total Quantity = SUM(FactSales[Quantity])
Average Order Value = DIVIDE([Total Sales], [Total Orders], 0)
Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0)
Average Profit per Order = DIVIDE([Total Profit], [Total Orders], 0)
Average Selling Price = DIVIDE([Total Sales], [Total Quantity], 0)
Average Discount = AVERAGE(FactSales[Discount])
```

## Time-Intelligence
```dax
YTD Sales = TOTALYTD([Total Sales], DimDate[Date])
YTD Profit = TOTALYTD([Total Profit], DimDate[Date])
Previous Year Sales = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(DimDate[Date]))
YoY Growth % = DIVIDE([Total Sales] - [Previous Year Sales], [Previous Year Sales], 0)
Running Total = CALCULATE([Total Sales], FILTER(ALL(DimDate), DimDate[Date] <= MAX(DimDate[Date])))
```

## Calculated Columns (DimCustomer)
```dax
Age Group = 
SWITCH(
    TRUE(),
    DimCustomer[Customer_Age] < 25, "18-24",
    DimCustomer[Customer_Age] < 35, "25-34",
    DimCustomer[Customer_Age] < 50, "35-49",
    DimCustomer[Customer_Age] >= 50, "50+",
    "Unknown"
)
```

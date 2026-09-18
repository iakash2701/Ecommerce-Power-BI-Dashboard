# E-Commerce Sales & Customer Analytics Dashboard 📊

## Project Overview
This project is an end-to-end Data Analytics Business Intelligence solution created using Microsoft Power BI Desktop. The dashboard analyzes over 10,000 sales records to uncover critical business insights regarding regional performance, product profitability, and customer segmentation.

## Business Problem
ShopSphere (a fictional e-commerce company) was experiencing high sales volume but lacked visibility into actual profit margins. Management needed an automated, interactive dashboard to identify "High Sales, Low Profit" traps caused by aggressive discounting strategies.

## Objectives
- Extract, transform, and load (ETL) raw transactional data into Power BI.
- Clean and standardize data using **Power Query**.
- Design a high-performance **Star Schema** data model.
- Write advanced **DAX** measures for Time-Intelligence and KPIs.
- Design an interactive, multi-page dashboard for Executive Management.

## Tools & Technologies
- **Microsoft Power BI Desktop:** Power Query, Data Modeling, DAX, Data Visualization
- **Python:** Synthetic data generation

## Data Pipeline
1. **Raw Data:** Over 10k rows of transactional e-commerce data containing intentional data quality issues.
2. **Data Cleaning (Power Query):** Removed duplicates, handled missing values, standardized text casing, corrected data types, and filtered invalid transaction statuses.
3. **Data Model:** Transformed flat file into a Star Schema with 1 Fact Table (`FactSales`) and 3 Dimension Tables (`DimProduct`, `DimCustomer`, `DimDate`).
4. **DAX Calculations:** Created core KPIs and Time-Intelligence metrics (YTD, YoY Growth, MoM Growth).

## Dashboard Pages
1. **Executive Overview:** High-level KPIs and monthly revenue trends.
2. **Sales Analysis:** Drill-down capabilities from Year ➡️ Quarter ➡️ Month and Category ➡️ Sub-category.
3. **Customer Analytics:** Demographic breakdowns and top customer leaderboards.
4. **Profitability Analysis:** Scatter charts identifying products operating at a net loss due to excessive discounting.
5. **Product Performance:** Conditional formatting identifying the Top 10 and Bottom 10 products by profit margin.

## Key Insights
* **The Discount Trap:** Products with an average discount exceeding 10% generated negative returns despite high sales volumes.
* **Corporate Dominance:** The Corporate customer segment drove ₹110M+ in revenue, significantly outperforming individual Consumers.
* **Top Product Risk:** Laptops alone generated ₹56M+ in revenue, indicating a heavy reliance on a single product category.

## Business Recommendations
1. **Cap Discounts:** Immediately restrict maximum allowable discounts for standard Consumer transactions to 5% to recover profit margins.
2. **Corporate Contracts:** Shift Corporate clients to fixed annual contracts instead of variable per-order discounting.
3. **Liquidate Bottom 10:** Discontinue the lowest-performing products tying up warehouse capital.

## How to Run
1. Download the `Ecommerce_Sales_Customer_Analytics.pbix` file.
2. Open it using Microsoft Power BI Desktop.
3. Interact with the slicers, drill-down arrows, and tooltips!

## Future Improvements
- Integrate an SQL database (e.g., PostgreSQL) to act as the primary data source via DirectQuery.
- Add predictive forecasting to the line charts using Power BI's built-in ML tools.

---
**Author:** Akash
**LinkedIn:** [Your LinkedIn URL Placeholder]

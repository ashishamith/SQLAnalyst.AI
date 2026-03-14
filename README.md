# SQLAnalyst.ai

AI-Powered Automated Sales Intelligence Platform

SQLAnalyst.ai is an end-to-end automated analytics system that converts raw SQL sales data into actionable business intelligence delivered automatically to managers every morning.

The system extracts sales KPIs from a SQL database, analyzes trends using AI, generates executive insights, and sends a daily automated sales report via email.

Additionally, the platform includes a real-time monitoring dashboard built with Streamlit and a business intelligence dashboard built with Power BI.

This project demonstrates how modern analytics teams integrate SQL analytics, workflow automation, AI insights, and dashboards to build automated data intelligence systems.

---

# Project Objective

In many organizations, managers manually run SQL queries, check dashboards, analyze metrics, and prepare daily reports. This process is time-consuming and delays decision-making.

SQLAnalyst.ai automates the entire workflow so managers receive a clear executive briefing every morning without manual analysis.

The system continuously monitors sales data, computes KPIs, generates AI-powered insights, and delivers a structured sales performance report.

---

# Key Features

## Automated KPI Extraction

The system extracts business metrics directly from the SQL sales database.

KPIs include:

• Daily Revenue  
• Previous Day Revenue  
• Revenue Change Percentage  
• Total Orders  
• Top 3 Revenue Generating Products  

These metrics are calculated using SQL queries.

---

## AI Generated Business Insights

The KPI results are sent to a Large Language Model which produces structured executive insights including:

• Executive Summary  
• Revenue Trend Insight  
• Product Contribution Insight  
• Business Risk Signal  
• Strategic Recommendation  

This converts raw metrics into actionable business intelligence.

---

## Automated Morning Executive Report

Every morning at 7:00 AM, the system automatically:

1. Extracts the latest KPIs from the database  
2. Sends KPI data to the AI model  
3. Generates executive insights  
4. Formats the report into HTML  
5. Sends the report via email to managers  

Managers begin the day with a clear overview of sales performance.

---

# Example Executive Email Report

Daily Sales Report

Revenue: $45,230  
Change vs Previous Day: +12.5%  
Total Orders: 312  

Top Performing Products  
Product A - $12,400  
Product B - $10,150  
Product C - $8,900  

Executive Summary  
Sales performance improved compared to the previous day due to increased demand for Product A.

Revenue Trend Insight  
Revenue growth of 12.5% indicates strong short-term sales momentum.

Product Contribution Insight  
The top three products generated the majority of total revenue.

Business Signal  
Risk Level: Low  
Recommendation: Maintain inventory levels and monitor product demand.

---

# System Architecture

Sales Database (MySQL)
        │
        ▼
SQL KPI Extraction
        │
        ▼
Workflow Automation (n8n)
        │
        ├── AI Insight Generation (LLM)
        ├── Google Sheets Logging
        └── Email Delivery (Gmail)
        │
        ▼
Executive Sales Report
        │
        ▼
Manager Receives Daily Brief
        │
        ├── Streamlit Monitoring Dashboard
        └── Power BI Business Intelligence Dashboard

---

# Data Pipeline

The platform runs two automated workflows.

## Continuous Monitoring Workflow

Runs periodically to detect new sales records.

Steps:

1. Detect new transactions  
2. Calculate updated KPIs  
3. Store results in Google Sheets  
4. Update monitoring dashboards  

---

## Morning Executive Workflow

Runs daily at 07:00 AM.

Steps:

1. Query latest sales KPIs  
2. Send KPI data to AI model  
3. Generate executive insights  
4. Send automated email report  

---

# Dashboards

## Streamlit Monitoring Dashboard

The Streamlit dashboard provides real-time operational monitoring.

Features:

• Live KPI tracking  
• Revenue trend visualization  
• Product performance analysis  
• Data pipeline monitoring  

Run the dashboard:

```
streamlit run dashboard.py
```

---

## Power BI Business Intelligence Dashboard

Power BI provides deeper analytics including:

• Revenue trend analysis  
• Product contribution breakdown  
• Sales performance metrics  
• Executive KPI summaries  

This dashboard is used for strategic decision making.

---

# Technology Stack

Database: MySQL  
Workflow Automation: n8n  
AI Insight Engine: OpenAI / OpenRouter  
Data Logging: Google Sheets  
Monitoring Dashboard: Streamlit  
Business Intelligence: Power BI  
Programming Language: Python  
Query Language: SQL  

---

# Project Structure

```
SQLAnalyst.ai
│
├── workflows
│   └── n8n_sales_automation.json
│
├── dashboards
│   ├── streamlit_dashboard.py
│   └── powerbi_dashboard.pbix
│
├── sql
│   └── sales_kpi_queries.sql
│
├── docs
│   └── architecture_diagram.png
│
└── README.md
```

---

# Setup Instructions

Install dependencies

```
pip install streamlit pandas mysql-connector-python
```

Run Streamlit dashboard

```
streamlit run dashboard.py
```

Setup n8n workflow

1. Import the workflow JSON file  
2. Connect credentials:

• MySQL database  
• Gmail account  
• Google Sheets account  
• OpenAI / OpenRouter API  

3. Activate the workflow triggers.

---

# Future Improvements

• AI based sales forecasting  
• anomaly detection alerts  
• Slack or Teams notifications  
• customer segmentation analytics  
• integration with cloud data warehouses  

---

# Skills Demonstrated

• SQL analytics and KPI engineering  
• workflow automation pipelines  
• AI powered business intelligence  
• dashboard development  
• end-to-end data pipeline architecture  

This project reflects modern analytics engineering practices used in production environments.

---

# License

MIT License

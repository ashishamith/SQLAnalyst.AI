SQLAnalyst.ai

AI-Powered Automated Sales Intelligence Platform

SQLAnalyst.ai is an automated business intelligence system that converts raw SQL sales data into actionable executive insights delivered every morning.

The platform continuously monitors transactional data, computes key business KPIs, generates AI-powered executive analysis, and distributes a daily sales intelligence report directly to managers via email.

In addition, the system provides real-time monitoring dashboards (Streamlit) and strategic analytics dashboards (Power BI) for operational and business decision-making.

The goal of this project is to demonstrate how SQL analytics, workflow automation, and AI-generated insights can be combined into a production-style analytics pipeline.

Problem Statement

In many organizations, managers must manually:

run SQL queries

check dashboards

analyze performance trends

prepare daily business reports

This process is time-consuming and delays decision-making.

SQLAnalyst.ai solves this by automating the entire analytics workflow, ensuring that managers receive a clear, structured executive briefing every morning before the workday begins.

Key Features
Automated KPI Extraction

The system automatically calculates daily sales KPIs directly from the transactional SQL database.

Metrics include:

Daily Revenue

Previous Day Revenue

Revenue Change Percentage

Total Orders

Top 3 Revenue-Generating Products

All calculations are performed using optimized SQL queries.

AI-Generated Executive Insights

The KPI data is sent to a Large Language Model which produces a structured executive report containing:

Executive Summary

Revenue Trend Insight

Product Contribution Insight

Business Risk Signal

Strategic Recommendation

This transforms raw metrics into decision-ready business intelligence.

Automated Morning Executive Report

Every morning at 7:00 AM, the system automatically:

Extracts latest KPIs from the sales database

Generates AI-driven business insights

Formats results into an executive email report

Sends the report directly to managers

This ensures leadership teams begin the day with clear visibility into business performance.

Real-Time Monitoring

The platform also includes a Streamlit dashboard used for operational monitoring of the analytics pipeline.

Capabilities include:

Live KPI tracking

Revenue trend visualization

Product performance analysis

Data pipeline monitoring

Strategic Business Intelligence

A Power BI dashboard provides deeper business analytics including:

Revenue growth trends

Product revenue contribution

Sales distribution analysis

Executive KPI summaries

This dashboard is designed for long-term business insights and decision support.

System Architecture
                 Sales Database
                     (MySQL)
                        │
                        ▼
             KPI Extraction Layer
                (SQL Queries)
                        │
                        ▼
             Workflow Automation
                    (n8n)
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
 AI Insight Engine   Data Logging    Email Delivery
 (LLM via API)     (Google Sheets)   (Gmail API)
        │
        ▼
 Executive Sales Report
        │
        ▼
 Manager Receives Daily Briefing
        │
        ├──────── Streamlit Monitoring Dashboard
        │
        └──────── Power BI Business Intelligence Dashboard
Data Pipeline Overview

The analytics pipeline operates in two automated workflows.

Continuous Monitoring Workflow

Runs periodically to detect new sales records.

Process:

Check latest order ID

Detect new transactions

Recompute KPIs

Log results to Google Sheets

Update monitoring dashboards

Morning Executive Workflow

Runs daily at 07:00 AM.

Process:

Query latest sales KPIs

Send KPI data to AI model

Generate executive insights

Format results into HTML report

Send email briefing to manager

Example Executive Report

Daily Sales Intelligence Report

Revenue: $45,230
Revenue Change vs Yesterday: +12.5%
Total Orders: 312

Top Performing Products
Product A — $12,400
Product B — $10,150
Product C — $8,900

Executive Summary
Sales performance improved compared to the previous day with strong demand for Product A.

Revenue Trend Insight
Revenue growth of 12.5% indicates positive short-term momentum.

Product Contribution Insight
The top three products generated the majority of total revenue.

Business Signal
Risk Level: Low
Recommendation: Maintain current inventory levels and monitor product demand.

Technology Stack
Layer	Technology
Database	MySQL
Workflow Automation	n8n
AI Insight Generation	OpenAI / OpenRouter
Data Logging	Google Sheets
Monitoring Dashboard	Streamlit
Business Intelligence	Power BI
Query Language	SQL
Programming	Python
Repository Structure
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
Running the Project
Install Python Dependencies
pip install streamlit pandas mysql-connector-python
Run Monitoring Dashboard
streamlit run dashboard.py
Setup n8n Workflow

Import the workflow JSON file

Configure credentials:

MySQL

Gmail

Google Sheets

OpenAI / OpenRouter

Activate the workflow triggers

Future Improvements

Potential extensions for the platform include:

Sales forecasting using machine learning

Automated anomaly detection

Slack or Teams alerts for business risks

Customer segmentation analytics

Integration with a cloud data warehouse

Real-time streaming analytics

Skills Demonstrated

This project demonstrates practical experience with:

SQL analytics and KPI engineering

Workflow automation pipelines

AI-driven business intelligence

Dashboard development

End-to-end data systems design

The architecture reflects modern analytics engineering and data platform practices used in production environments.

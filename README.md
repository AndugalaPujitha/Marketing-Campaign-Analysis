# 📊 Marketing Campaign Analysis Pipeline

A complete end-to-end marketing campaign analysis project built using **Python, SQL, and Tableau**, transforming raw customer data into actionable business insights through a structured ETL pipeline and interactive dashboards.

This project simulates a **real-world banking/marketing analytics workflow**, focusing on customer response behavior, campaign effectiveness, and data-driven decision-making.

---

## 🎯 Project Objective

The primary goal of this project is to analyze marketing campaign data to:

- Identify high-performing customer segments  
- Evaluate campaign effectiveness  
- Understand factors influencing customer response  
- Build interactive dashboards for business insights  

---

## 📌 Business Objective

This project helps marketing teams and analysts to:

- Measure campaign success using response rates  
- Identify target customer segments for better conversion  
- Optimize campaign strategies based on data insights  
- Improve decision-making through visual analytics  

---

## 📊 Tools & Technologies

| Tool | Purpose |
|------|--------|
| Python (Pandas, NumPy) | Data cleaning, transformation, feature engineering |
| SQLite / SQL | Data storage, querying, KPI extraction |
| Tableau | Interactive dashboard and visualization |
| Excel / CSV | Raw data source |

---

## 🔁 End-to-End Workflow
```
Raw CSV Data
↓
Python (Data Cleaning + Feature Engineering)
↓
SQL (Storage + Querying KPIs)
↓
Tableau (Dashboard + Insights)
```

This pipeline mimics a **real industry ETL + BI workflow** used in marketing and analytics teams.

---

## 🧹 Data Processing (Python)

- Loaded dataset using Pandas  
- Converted categorical response (`yes/no`) into binary (1/0)  
- Handled missing values and cleaned data  
- Created new features:
  - Age Groups  
  - Contact Efficiency  
- Encoded categorical variables for analysis  

---

## 🗃 Database & SQL Layer

- Stored processed data into SQLite database  
- Created structured table: `campaign_data`  
- Executed SQL queries to extract KPIs such as:
  - Response Rate  
  - Campaign Effectiveness  
  - Customer Segment Performance  

---

## 📊 Key KPIs Analyzed

- **Response Rate** → Percentage of customers who responded  
- **Campaign Efficiency** → Effectiveness of contact attempts  
- **Customer Segmentation** → Response by age, job, etc.  
- **Previous Campaign Impact** → Influence of past outcomes  

---

## 📈 Tableau Dashboard

An interactive dashboard was built to visualize:

- Customer segmentation (Age, Job)  
- Campaign performance trends  
- Response rate analysis  
- Previous campaign impact  

### 🔹 Features:
- KPI cards for quick insights  
- Interactive filters (Age Group, Job, Campaign)  
- Clean and intuitive layout for business users  

---

## 🧠 Key Insights

- Customers aged **26–35 showed the highest response rate**  
- Fewer campaign contacts resulted in better conversion  
- Previous successful campaigns significantly increased response probability  
- Certain job segments performed better in engagement  

---

## ⚙️ How to Run This Project

1. Clone the repository  
```bash
git clone <your-repo-link>
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run analysis pipeline
```
python src/analysis.py
```
4. Open Tableau dashboard
- Load outputs/cleaned_data.csv
- Explore interactive visuals

---
## 📂 Project Structure
```
Marketing-Campaign-Analysis/
│
├── data/
├── src/
├── sql/
├── dashboard/
├── outputs/
├── marketing.db
├── README.md
└── requirements.txt
```
---

## 🚀 Project Highlights

- Built a complete ETL pipeline from raw data to insights
- Applied real-world marketing analytics concepts
- Developed interactive Tableau dashboards
- Generated actionable business insights

---

## 📌 Conclusion

- This project demonstrates strong skills in:
- Data cleaning and transformation
- SQL-based analysis
- Business intelligence and visualization
- Translating data into actionable insights

---

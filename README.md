# Interactive Business Dashboard — Global Superstore

DevelopersHub Corporation — Data Science & Analytics Advanced Internship, Task 5.

## 🎯 Objective
Develop an interactive dashboard for analyzing sales, profit, and segment-wise performance across a retail business.

## 🗂️ Dataset
Structured to match the **Global Superstore Dataset** (Order ID, Order Date, Customer Name, Region, Category, Sub-Category, Quantity, Sales, Profit). A synthetic 5,000-row dataset with realistic seasonal, regional, and category-level sales/profit patterns is included at `data/global_superstore.csv`.

## 🧠 Approach
1. Cleaned and prepared the dataset (de-duplication, profit margin, monthly period column) — full EDA is in `notebook.ipynb`.
2. Explored sales/profit trends, regional performance, and category profitability in the notebook.
3. Built an interactive **Streamlit** dashboard (`app.py`) with sidebar filters for **Region**, **Category**, **Sub-Category**, and **Order Date range**.
4. Displayed key KPIs: **Total Sales**, **Total Profit**, **Profit Margin**, **Order Count**.
5. Added charts: Sales by Region, Sales vs Profit by Category, Monthly Sales Trend, and **Top 5 Customers by Sales**.

## 📊 Results & Findings
- Technology and Office Supplies categories drive most of the profit; Furniture has thin (sometimes negative) margins at higher discount levels — see notebook for the discount-vs-profit analysis.
- Sales show a clear seasonal pattern with peaks toward year-end.
- The dashboard's filters let a business user drill into any Region × Category × Sub-Category combination and immediately see the KPI and top-customer impact.

## 🛠️ Tech Stack
`pandas` · `streamlit` · `matplotlib` · `seaborn`

## ▶️ How to Run

**Notebook (EDA & analysis):**
```bash
pip install -r requirements.txt
jupyter notebook notebook.ipynb
```

**Dashboard:**
```bash
pip install -r requirements.txt
streamlit run app.py
```
Then open the local URL Streamlit prints (usually http://localhost:8501).

## 📁 Repository Structure
```
task5-superstore-dashboard/
├── data/
│   └── global_superstore.csv
├── notebook.ipynb
├── app.py
├── requirements.txt
└── README.md
```

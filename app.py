"""
Interactive Business Dashboard — Global Superstore
Run with:  streamlit run app.py
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Superstore Business Dashboard", layout="wide")
sns.set_style("whitegrid")


@st.cache_data
def load_data():
    df = pd.read_csv("data/global_superstore.csv", parse_dates=["Order Date"])
    df = df.drop_duplicates(subset="Order ID")
    df["Profit Margin"] = (df["Profit"] / df["Sales"]).round(3)
    df["Order Month"] = df["Order Date"].dt.to_period("M").astype(str)
    return df


df = load_data()

st.title("Global Superstore — Business Performance Dashboard")
st.caption("Filter by Region, Category, and Sub-Category to explore Sales & Profit KPIs.")

# ---------------- Sidebar filters ----------------
st.sidebar.header("Filters")

regions = sorted(df["Region"].unique())
sel_regions = st.sidebar.multiselect("Region", regions, default=regions)

categories = sorted(df["Category"].unique())
sel_categories = st.sidebar.multiselect("Category", categories, default=categories)

subcats_available = sorted(df[df["Category"].isin(sel_categories)]["Sub-Category"].unique())
sel_subcats = st.sidebar.multiselect("Sub-Category", subcats_available, default=subcats_available)

date_min, date_max = df["Order Date"].min(), df["Order Date"].max()
date_range = st.sidebar.date_input("Order Date Range", (date_min, date_max),
                                    min_value=date_min, max_value=date_max)

filtered = df[
    df["Region"].isin(sel_regions)
    & df["Category"].isin(sel_categories)
    & df["Sub-Category"].isin(sel_subcats)
]
if isinstance(date_range, tuple) and len(date_range) == 2:
    start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    filtered = filtered[(filtered["Order Date"] >= start) & (filtered["Order Date"] <= end)]

if filtered.empty:
    st.warning("No data matches the selected filters. Please broaden your selection.")
    st.stop()

# ---------------- KPIs ----------------
total_sales = filtered["Sales"].sum()
total_profit = filtered["Profit"].sum()
margin = total_profit / total_sales if total_sales else 0
orders = filtered["Order ID"].nunique()

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Sales", f"${total_sales:,.0f}")
k2.metric("Total Profit", f"${total_profit:,.0f}")
k3.metric("Profit Margin", f"{margin:.1%}")
k4.metric("Orders", f"{orders:,}")

st.divider()

# ---------------- Charts ----------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Region")
    fig, ax = plt.subplots()
    filtered.groupby("Region")["Sales"].sum().sort_values().plot(kind="barh", ax=ax, color="#4C72B0")
    ax.set_xlabel("Sales ($)")
    st.pyplot(fig)

with col2:
    st.subheader("Sales vs Profit by Category")
    fig, ax = plt.subplots()
    filtered.groupby("Category")[["Sales", "Profit"]].sum().plot(kind="bar", ax=ax)
    plt.xticks(rotation=0)
    st.pyplot(fig)

st.subheader("Monthly Sales Trend")
fig, ax = plt.subplots(figsize=(11, 4))
monthly = filtered.groupby("Order Month")["Sales"].sum().sort_index()
monthly.plot(ax=ax, marker="o", color="#55A868")
ax.set_ylabel("Sales ($)")
plt.xticks(rotation=60)
st.pyplot(fig)

st.subheader("Top 5 Customers by Sales")
top5 = filtered.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(5)
c1, c2 = st.columns([1, 1])
with c1:
    st.dataframe(top5.reset_index().rename(columns={"Sales": "Total Sales ($)"}), use_container_width=True)
with c2:
    fig, ax = plt.subplots()
    top5.sort_values().plot(kind="barh", ax=ax, color="#C44E52")
    ax.set_xlabel("Sales ($)")
    st.pyplot(fig)

with st.expander("View filtered raw data"):
    st.dataframe(filtered.sort_values("Order Date", ascending=False), use_container_width=True)

# app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# ---------- Load Data ----------
BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "clean_retail_data.csv"
df = pd.read_csv(csv_path)

# ---------- App Config ----------
st.set_page_config(page_title="Retail Profitability Dashboard", layout="wide")

# ---------- Introduction ----------
st.title(" Retail Profitability Dashboard - ADTA 5410 : Team 2")
st.markdown("""
## Introduction
**Business Problem:**  
How can we identify the key drivers of product-level profitability and build a model to predict whether a transaction will be **high-profit** or **low-profit** based on internal and competitive features?

**Business Value:**  
- Optimize pricing and discounting strategies  
- Allocate ad spend more effectively  
- Avoid low-margin products  
- Make data-driven profit decisions
""")

# ---------- Data Exploration ----------
st.markdown("## Data Exploration")

# Sidebar for column selection
numeric_cols = df.select_dtypes(include='number').columns.tolist()
selected_col = st.selectbox("Select a numerical column to explore", numeric_cols)

# Univariate Plot
st.markdown("### Univariate Analysis")
fig1, ax1 = plt.subplots()
sns.histplot(df[selected_col], kde=True, ax=ax1)
st.pyplot(fig1)

# Bivariate Analysis
st.markdown("### Bivariate Analysis")
target_col = st.selectbox("Choose target/profit class column", df.columns)
if target_col in df.columns:
    fig2, ax2 = plt.subplots()
    sns.boxplot(data=df, x=target_col, y=selected_col, ax=ax2)
    st.pyplot(fig2)

# Multivariate Analysis
st.markdown("### Multivariate Analysis")
corr = df[numeric_cols].corr()
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax3)
st.pyplot(fig3)

# ---------- Insights ----------
st.markdown("## Insights")

st.markdown("""
- Some internal cost features (like referral fees, FBA costs) are strongly correlated with profit margins.
- Competitor pricing can dilute margin on high-cost items — especially where price gaps are minimal.
- A clear separation exists between high- and low-profit transactions in terms of advertising spend and unit economics.
""")

# ---------- Recommendations ----------
st.markdown("## Recommendations")

st.markdown("""
- **Adjust price gaps** dynamically for products with weak competitor advantage.
- **Reduce ad budget** on SKUs that remain low-profit despite promotion.
- **Bundle or discontinue** low-margin items with high fulfillment costs.
""")

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, get_top_regions

st.set_page_config(page_title="GHI Dashboard", layout="wide")
st.title("Global Hunger Index Dashboard")

# Load data
data = load_data()

# Country selector
selected_country = st.selectbox("Select a Country", data["Country"].unique())

# Boxplot of GHI
st.subheader(f"GHI Boxplot for {selected_country}")
fig, ax = plt.subplots()
sns.boxplot(data=data[data["Country"] == selected_country], y="GHI", ax=ax)
st.pyplot(fig)

# Top regions table
st.subheader("Top 5 Regions by Lowest GHI")
top_regions = get_top_regions(data)
st.dataframe(top_regions)
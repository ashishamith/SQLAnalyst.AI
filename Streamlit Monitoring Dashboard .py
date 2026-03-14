import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import time

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="🚀 Sales War Room",
    page_icon="🔥",
    layout="wide"
)

# -------------------------
# CUSTOM GAMING CSS
# -------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Orbitron', sans-serif;
}

body {
    background: radial-gradient(circle at top left, #0f0c29, #302b63, #24243e);
}

.metric-box {
    background: linear-gradient(145deg, #111122, #1c1c3a);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 0px 20px #00f5ff;
    text-align: center;
    transition: 0.3s;
}

.metric-box:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 40px #ff00c8;
}

.metric-title {
    font-size: 18px;
    color: #aaa;
}

.metric-value {
    font-size: 38px;
    font-weight: bold;
    background: linear-gradient(to right, #00f5ff, #ff00c8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.section-title {
    font-size: 28px;
    margin-top: 40px;
    color: #00f5ff;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# GOOGLE SHEET CSV LINK
# -------------------------
sheet_url = "https://docs.google.com/spreadsheets/d/1f3PjJTWav3xmN2vevmgx7wQznfkuWjNeViKHdO5mDQE/export?format=csv"

@st.cache_data(ttl=60)
def load_data():
    df = pd.read_csv(sheet_url)

    # Clean numeric columns
    df["revenue"] = pd.to_numeric(df.get("revenue"), errors="coerce")
    df["orders"] = pd.to_numeric(df.get("orders"), errors="coerce")
    df["revenue_change_percent"] = pd.to_numeric(df.get("revenue_change_percent"), errors="coerce")

    # Convert date column if exists
    if "report_date" in df.columns:
        df["report_date"] = pd.to_datetime(df["report_date"], errors="coerce")

    return df

df = load_data()

if df.empty:
    st.error("No data found in Google Sheet.")
    st.stop()

latest = df.iloc[-1]

# -------------------------
# DATA
# -------------------------
revenue = latest.get("revenue", 0)
orders = latest.get("orders", 0)
change = latest.get("revenue_change_percent", 0)
top_products = latest.get("top_3_products", "")

# Handle NaN safely
revenue = 0 if pd.isna(revenue) else revenue
orders = 0 if pd.isna(orders) else orders
change = 0 if pd.isna(change) else change

# -------------------------
# HEADER
# -------------------------
st.title("🔥 SALES WAR ROOM")
st.markdown("### Live Performance Monitoring System")

# -------------------------
# KPI SECTION
# -------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">💰 TOTAL REVENUE</div>
        <div class="metric-value">${revenue:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">📦 TOTAL ORDERS</div>
        <div class="metric-value">{int(orders)}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    color = "#00ff88" if change >= 0 else "#ff4b4b"

    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">📊 PROFIT / LOSS %</div>
        <div class="metric-value" style="color:{color}">
            {change:.1f}%
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# REVENUE TREND GRAPH
# -------------------------
st.markdown('<div class="section-title">📈 Revenue Trend</div>', unsafe_allow_html=True)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["report_date"],
    y=df["revenue"],
    mode="lines+markers",
    line=dict(color="#00f5ff", width=4),
    marker=dict(size=10, color="#ff00c8")
))

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white"),
    xaxis_title="Date",
    yaxis_title="Revenue"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# TOP PRODUCTS
# -------------------------
st.markdown('<div class="section-title">🔥 Top Performing Products</div>', unsafe_allow_html=True)

if isinstance(top_products, str) and top_products.strip() != "":
    products = top_products.split("\n")

    for p in products:
        st.markdown(f"""
        <div style="
            background: linear-gradient(90deg,#ff00c8,#00f5ff);
            padding:15px;
            border-radius:10px;
            margin-bottom:10px;
            font-size:18px;
            color:black;
            font-weight:bold;">
            {p}
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("No product data available")

# -------------------------
# ORDERS VS REVENUE
# -------------------------
st.markdown('<div class="section-title">📊 Orders vs Revenue</div>', unsafe_allow_html=True)

fig2 = px.bar(
    df.tail(7),
    x="report_date",
    y=["orders", "revenue"],
    barmode="group",
    template="plotly_dark"
)

fig2.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# AUTO REFRESH
# -------------------------
time.sleep(60)
st.rerun()

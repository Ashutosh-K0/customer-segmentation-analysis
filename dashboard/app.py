import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

/* Main App Background */
.main {
    background-color: #0E1117;
}

/* Dashboard Title */
h1 {
    color: white;
    text-align: center;
    font-size: 42px;
    padding-bottom: 10px;
}

/* Section Headers */
h2, h3 {
    color: white;
}

/* Sidebar Styling */
section[data-testid="stSidebar"] {
    background-color: #161A23;
}

/* KPI Metric Cards */
div[data-testid="metric-container"] {
    background-color: #1E2430;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #2D3648;
}

/* Dataframe Styling */
div[data-testid="stDataFrame"] {
    border-radius: 10px;
}

/* Alert Box */
div[data-testid="stAlert"] {
    border-radius: 10px;
}

/* Reduce top padding */
.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------

df = pd.read_csv("data/Mall_Customers.csv")

# Rename columns
df.columns = [
    "customer_id",
    "gender",
    "age",
    "annual_income",
    "spending_score"
]

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------

st.sidebar.title("Dashboard Filters")

# Gender Filter
gender_filter = st.sidebar.multiselect(
    "Select Gender",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)

# Age Filter
age_filter = st.sidebar.slider(
    "Select Age Range",
    int(df["age"].min()),
    int(df["age"].max()),
    (
        int(df["age"].min()),
        int(df["age"].max())
    )
)

# Income Filter
income_filter = st.sidebar.slider(
    "Select Annual Income Range",
    int(df["annual_income"].min()),
    int(df["annual_income"].max()),
    (
        int(df["annual_income"].min()),
        int(df["annual_income"].max())
    )
)

# Spending Score Filter
spending_filter = st.sidebar.slider(
    "Select Spending Score Range",
    int(df["spending_score"].min()),
    int(df["spending_score"].max()),
    (
        int(df["spending_score"].min()),
        int(df["spending_score"].max())
    )
)

# ---------------------------------------------------
# APPLY FILTERS
# ---------------------------------------------------

filtered_df = df[
    (df["gender"].isin(gender_filter)) &
    (df["age"] >= age_filter[0]) &
    (df["age"] <= age_filter[1]) &
    (df["annual_income"] >= income_filter[0]) &
    (df["annual_income"] <= income_filter[1]) &
    (df["spending_score"] >= spending_filter[0]) &
    (df["spending_score"] <= spending_filter[1])
]

# ---------------------------------------------------
# DASHBOARD HEADER
# ---------------------------------------------------

st.markdown("""
# Customer Segmentation Analysis Dashboard
""")

st.caption(
    "Interactive customer analytics and segmentation dashboard using Python, SQL, and Machine Learning"
)

st.write("")

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

st.subheader("Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric(
    label="Total Customers",
    value=len(filtered_df)
)

col2.metric(
    label="Average Income",
    value=f"${filtered_df['annual_income'].mean():.2f}k"
)

col3.metric(
    label="Average Spending Score",
    value=f"{filtered_df['spending_score'].mean():.2f}"
)

st.write("")

# ---------------------------------------------------
# AGE + GENDER DISTRIBUTION
# ---------------------------------------------------

col4, col5 = st.columns(2)

# Age Distribution
with col4:

    st.subheader("Age Distribution")

    fig1, ax1 = plt.subplots(figsize=(7,5))

    sns.histplot(
        filtered_df["age"],
        bins=20,
        kde=True,
        ax=ax1
    )

    ax1.set_xlabel("Age")
    ax1.set_ylabel("Customer Count")

    st.pyplot(fig1)

# Gender Distribution
with col5:

    st.subheader("Gender Distribution")

    fig2, ax2 = plt.subplots(figsize=(6,5))

    sns.countplot(
        data=filtered_df,
        x="gender",
        ax=ax2
    )

    st.pyplot(fig2)

st.write("")

# ---------------------------------------------------
# INCOME VS SPENDING ANALYSIS
# ---------------------------------------------------

st.subheader("Income vs Spending Analysis")

fig3, ax3 = plt.subplots(figsize=(10,6))

sns.scatterplot(
    data=filtered_df,
    x="annual_income",
    y="spending_score",
    hue="gender",
    s=100,
    ax=ax3
)

ax3.set_xlabel("Annual Income")
ax3.set_ylabel("Spending Score")

st.pyplot(fig3)

st.write("")

# ---------------------------------------------------
# K-MEANS CLUSTERING
# ---------------------------------------------------

# K-Means Clustering

st.subheader("Customer Segments using K-Means Clustering")

X = filtered_df[["annual_income", "spending_score"]]

if len(filtered_df) >= 5:

    kmeans = KMeans(
        n_clusters=5,
        init="k-means++",
        random_state=42
    )

    filtered_df["cluster"] = kmeans.fit_predict(X)

    # Cluster Names
    cluster_names = {
        0: "Standard Customers",
        1: "Premium Customers",
        2: "Impulsive Customers",
        3: "Careful Customers",
        4: "Budget Customers"
    }

    filtered_df["cluster_name"] = filtered_df["cluster"].map(cluster_names)

    # Visualization code here...

else:
    st.warning("Not enough data points for clustering.")

# Cluster Names
cluster_names = {
    0: "Standard Customers",
    1: "Premium Customers",
    2: "Impulsive Customers",
    3: "Careful Customers",
    4: "Budget Customers"
}

filtered_df["cluster_name"] = filtered_df["cluster"].map(cluster_names)

# Cluster Visualization
fig4, ax4 = plt.subplots(figsize=(10,7))

sns.scatterplot(
    data=filtered_df,
    x="annual_income",
    y="spending_score",
    hue="cluster_name",
    palette="Set2",
    s=120,
    ax=ax4
)

# Centroids
ax4.scatter(
    kmeans.cluster_centers_[:,0],
    kmeans.cluster_centers_[:,1],
    s=300,
    c='black',
    marker='X',
    label='Centroids'
)

ax4.set_xlabel("Annual Income")
ax4.set_ylabel("Spending Score")

st.pyplot(fig4)

st.write("")

# ---------------------------------------------------
# CLUSTER DISTRIBUTION
# ---------------------------------------------------

st.subheader("Cluster Distribution")

cluster_counts = filtered_df["cluster_name"].value_counts()

fig5, ax5 = plt.subplots(figsize=(8,5))

ax5.pie(
    cluster_counts,
    labels=cluster_counts.index,
    autopct='%1.1f%%'
)

st.pyplot(fig5)

st.write("")

# ---------------------------------------------------
# BUSINESS INSIGHTS
# ---------------------------------------------------

st.subheader("Business Insights")

st.success("""
• Premium customers show both high income and high spending behavior.

• Careful customers have high income but lower spending tendencies.

• Impulsive customers spend aggressively despite lower income.

• Budget customers show lower purchasing engagement.

• Standard customers represent the average customer population.
""")

st.write("")

# ---------------------------------------------------
# DATASET TABLE
# ---------------------------------------------------

st.subheader("Customer Dataset")

st.dataframe(filtered_df)
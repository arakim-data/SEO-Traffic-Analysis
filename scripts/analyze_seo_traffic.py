import pandas as pd

# data load
df = pd.read_csv("../data/sameple_seo_traffic_data.csv")

# basic data exploration
print("Data info:\n",df.info())
print("\n preview Top Data:\n", df.head())


# KPI analysis
total_sessions = df["Sessions"].sum()
avg_engagement_rate = df["Engagement Rate"].mean()

print(f"\n Total Sessions:{total_sessions}")
print(f"Average Engagement Rate:{avg_engagement_rate:.2f}%")


# The highest traffic source
top_source = df.loc[df["Sessions"].idxmax(),"Session Source"]
print(f"Toop Source:{top_source}")
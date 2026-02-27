#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
# Ensure output folder exists for annotated graphs
os.makedirs("final_graphs_annotated", exist_ok=True)

#loading files
file1 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar enrolment\\api_data_aadhar_enrolment_0_500000.csv"
file2 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar enrolment\\api_data_aadhar_enrolment_500000_1000000.csv"
file3 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar enrolment\\api_data_aadhar_enrolment_1000000_1006029.csv"
file4 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar_demographic\\api_data_aadhar_demographic_0_500000.csv"
file5 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar_demographic\\api_data_aadhar_demographic_500000_1000000.csv"
file6 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar_demographic\\api_data_aadhar_demographic_1000000_1500000.csv"
file7 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar_demographic\\api_data_aadhar_demographic_1500000_2000000.csv"
file8 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar_demographic\\api_data_aadhar_demographic_2000000_2071700.csv"
# Read CSV files
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)
dp1 = pd.read_csv(file4)
dp2 = pd.read_csv(file5)
dp3 = pd.read_csv(file6)
dp4 = pd.read_csv(file7)
dp5 = pd.read_csv(file8)

# Merge (append) all rows
df = pd.concat([df1, df2, df3], ignore_index=True)
dp = pd.concat([dp1, dp2, dp3, dp4, dp5], ignore_index=True)

print("Total rows after merging enrolment dataset:", df.shape[0])
print("Total columns in enrolment dataset:", df.shape[1])
print("Total rows after merging demographic dataset:", dp.shape[0])
print("Total columns in demographic dataset:", dp.shape[1])

# Show first 5 rows
print(df.head())
print(dp.head())

#Enrolment Dataset Preprocessing
# Convert date column (DD-MM-YYYY format)
df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")

# Create total enrolments column
df["total_enrolments"] = df["age_0_5"] + df["age_5_17"] + df["age_18_greater"]

# Create Month column
df["month"] = df["date"].dt.to_period("M").astype(str)

print(df.info())

#Creating One single Dataset File
#df.to_csv("aadhaar_enrolment_merged.csv", index=False)
#print("Saved as aadhaar_enrolment_merged.csv")

#Demographic Dataset Preprocessing
# Convert date column (DD-MM-YYYY format)
dp["date"] = pd.to_datetime(dp["date"], dayfirst=True, errors="coerce")

# Rename the incomplete age column safely
dp = dp.rename(columns={"demo_age_17_": "demo_age_17_plus"})

# Create total updates
dp["total_demo_updates"] = dp["demo_age_5_17"] + dp["demo_age_17_plus"]

# Month column
dp["month"] = dp["date"].dt.to_period("M").astype(str)

# Drop missing (small amount)
dp= dp.dropna(subset=["state","district","pincode","total_demo_updates"])

print("Cleaned Dataset 2 ready")
print(dp.info())

#Creating One single Dataset File
#dp.to_csv("aadhaar_demo_merged.csv", index=False)
#print("Saved as aadhaar_demo_merged.csv")

df["state"] = df["state"].str.strip().str.replace(r"\s+", " ", regex=True).str.title()
dp["state"] = dp["state"].str.strip().str.replace(r"\s+", " ", regex=True).str.title()

print(df.shape)
print(df.isna().sum())
print(df.dtypes)
print(df["date"].min(), df["date"].max())

print(dp.shape)
print(dp.isna().sum())
print(dp.dtypes)
print(dp["date"].min(), dp["date"].max())

# Summary Tables of enrolment dataset
# A) India Month-wise Trend
india_month = df.groupby("month")[["age_0_5","age_5_17","age_18_greater","total_enrolments"]].sum().reset_index()
india_month.head(10)

# Plotting the trend
india_month = df.groupby("month")["total_enrolments"].sum().reset_index()
plt.figure(figsize=(12,5))
plt.plot(india_month["month"], india_month["total_enrolments"], marker="o")
plt.xticks(rotation=45)
plt.title("India: Aadhaar Enrolments Trend (Month-wise)")
plt.xlabel("Month")
plt.ylabel("Total Enrolments")
plt.grid(True)
# Highlight peak month
peak_row = india_month.loc[india_month["total_enrolments"].idxmax()]
peak_month = peak_row["month"]
peak_value = peak_row["total_enrolments"]
plt.annotate(
    f"Peak: {peak_month}\n({peak_value:,})",
    xy=(peak_month, peak_value),
    xytext=(peak_month, peak_value * 1.05),
    arrowprops=dict(arrowstyle="->")
)
# Add total enrolments text on the graph
total_enrolments = df["total_enrolments"].sum()
plt.text(0.01, 0.95, f"Total Enrolments: {total_enrolments:,}",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top')

plt.tight_layout()
#plt.savefig("final_graphs_annotated/A1_india_monthly_trend_annotated.png", dpi=300)
plt.show()


# B) State Ranking
state_total = df.groupby("state")["total_enrolments"].sum().reset_index().sort_values(by="total_enrolments", ascending=False)
state_total.head(10)

top10_states = df.groupby("state")["total_enrolments"].sum().sort_values(ascending=False).head(10)
top10_states_sorted = top10_states.sort_values()

# Plotting the top 10 states Trend
plt.figure(figsize=(12,6))
bars = plt.barh(top10_states_sorted.index, top10_states_sorted.values)
plt.title("Top 10 States by Total Aadhaar Enrolments")
plt.xlabel("Total Enrolments")
plt.ylabel("State")
plt.grid(True)
# Add labels
for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2, f"  {int(width):,}", va='center')

plt.tight_layout()
#plt.savefig("final_graphs_annotated/A3_top10_states_enrol_annotated.png", dpi=300)
plt.show()

# C)Top Districts
top_districts = df.groupby(["state","district"])["total_enrolments"].sum().reset_index().sort_values(by="total_enrolments", ascending=False)
top_districts.head(10)

# Plotting the top 10 districts
top10_districts = df.groupby(["state","district"])["total_enrolments"].sum().sort_values(ascending=False).head(10)
print(top10_districts)
top10_districts = (
    df.groupby(["state","district"])["total_enrolments"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top10_districts_sorted = top10_districts.sort_values()

plt.figure(figsize=(12,6))
bars = plt.barh(
    [f"{s} - {d}" for s, d in top10_districts_sorted.index],
    top10_districts_sorted.values
)

plt.title("Top 10 Districts by Total Aadhaar Enrolments")
plt.xlabel("Total Enrolments")
plt.grid(True)

for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2, f"  {int(width):,}", va='center')

plt.tight_layout()
#plt.savefig("final_graphs_annotated/A4_top10_districts_enrol_annotated.png", dpi=300)
plt.show()


# D) Top Pincodes
top_pincodes = df.groupby(["state","district","pincode"])["total_enrolments"].sum().reset_index().sort_values(by="total_enrolments", ascending=False)
top_pincodes.head(10)

# Plotting the top 10 pincodes
top10_pincode = df.groupby(["state","district","pincode"])["total_enrolments"].sum().sort_values(ascending=False).head(10)
print(top10_pincode)
import matplotlib.pyplot as plt
import os

os.makedirs("final_graphs_annotated", exist_ok=True)

top_pincodes = (
    df.groupby(["state", "district", "pincode"])["total_enrolments"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_pincodes_sorted = top_pincodes.sort_values()

labels = [f"{s}-{d}-{p}" for (s, d, p) in top_pincodes_sorted.index]

plt.figure(figsize=(12,6))
bars = plt.barh(labels, top_pincodes_sorted.values)

plt.title("Top 10 PIN Codes by Aadhaar Enrolments (Hotspots)")
plt.xlabel("Total Enrolments")
plt.ylabel("State - District - PIN")
plt.grid(True)
# Add value labels
for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2, f"  {int(width):,}", va="center")

plt.tight_layout()
#plt.savefig("final_graphs_annotated/B3_top10_pincodes_enrol_labeled.png", dpi=300)
plt.show()


# E) State wise Growth Rate
state_month = (
    df.groupby(["state", "month"])["total_enrolments"]
    .sum()
    .reset_index()
)
# previous month value per state
state_month["prev"] = state_month.groupby("state")["total_enrolments"].shift(1)
# safe growth calculation (avoid divide-by-zero / inf)
state_month["growth_%"] = (
    (state_month["total_enrolments"] - state_month["prev"]) / state_month["prev"] * 100
)
# replace infinite values and drop missing growth entries
state_month["growth_%"] = state_month["growth_%"].replace([np.inf, -np.inf], pd.NA)
state_month = state_month.dropna(subset=["growth_%"])

# Top 10 spikes overall
top_spikes = state_month.sort_values("growth_%", ascending=False).head(10)

plt.figure(figsize=(12,6))
labels = top_spikes["state"] + " (" + top_spikes["month"] + ")"
bars = plt.barh(labels, top_spikes["growth_%"])

plt.title("Top 10 State-Month Enrolment Spikes (Anomaly Detection)")
plt.xlabel("Growth % vs Previous Month")
plt.ylabel("State (Month)")
plt.grid(True)

for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height() / 2, f"  {width:.1f}%", va="center")

plt.tight_layout()
#plt.savefig("final_graphs_annotated/A8_anomaly_spikes_annotated.png", dpi=300)
plt.show()




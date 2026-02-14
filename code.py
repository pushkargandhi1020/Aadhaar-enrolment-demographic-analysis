#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#loading files
file1 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar enrolment\\api_data_aadhar_enrolment_0_500000.csv"
file2 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar enrolment\\api_data_aadhar_enrolment_500000_1000000.csv"
file3 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar enrolment\\api_data_aadhar_enrolment_1000000_1006029.csv"
file4 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar demographic\\api_data_aadhar_demographic_0_500000.csv"
file5 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar demographic\\api_data_aadhar_demographic_500000_1578742.csv"
file6 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar demographic\\api_data_aadhar_demographic_1578742_2133894.csv"
file7 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar demographic\\api_data_aadhar_demographic_1500000_2000000.csv"
file8 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar demographic\\api_data_aadhar_demographic_2000000_2133894.csv"

# Read Excel files
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
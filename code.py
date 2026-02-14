#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#loading files
file1 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar enrolment\\api_data_aadhar_enrolment_0_500000.csv"
file2 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar enrolment\\api_data_aadhar_enrolment_500000_1000000.csv"
file3 = "C:\\Users\\pushk\\OneDrive\\Desktop\\Aadhar Hacktahon Project\\Aadhaar-enrolment-demographic-analysis\\data\\aadhar enrolment\\api_data_aadhar_enrolment_1000000_1006029.csv"

# Read CSV files
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)

# Merge (append) all rows
df = pd.concat([df1, df2, df3], ignore_index=True)

print("Total rows after merging enrolment dataset:", df.shape[0])
print("Total columns in enrolment dataset:", df.shape[1])

# Show first 5 rows
print(df.head())
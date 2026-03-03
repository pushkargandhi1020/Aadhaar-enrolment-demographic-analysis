# Aadhaar-enrolment-demographic-analysis
Aadhaar Enrolment & Demographic Trends Analysis (India)
Overview
This project presents a comprehensive data-driven analysis of Aadhaar enrolment and demographic update activities across India. Using large-scale aggregated datasets, the analysis uncovers societal trends, geographic hotspots, seasonal patterns, anomalies, and operational KPIs to support better service planning and resource allocation.
The project was developed as part of UIDAI Hackathon 2026 and focuses on transforming raw public data into actionable insights using Python-based analytics.
________________________________________
## Objectives

- Analyze time-based trends in Aadhaar enrolments and demographic updates  
- Identify age-wise societal patterns in enrolment and update behavior  
- Detect state, district, and PIN code hotspots  
- Perform anomaly detection to capture unusual spikes in demand  
- Design a combined KPI (Updates-to-Enrolment Ratio) for workload assessment  
- Propose data-backed recommendations for operational planning  

## Key Insights

- Aadhaar enrolment demand is child-driven:
  - Age 0–5 contributes ~65%  
  - Age 5–17 contributes ~32%  
  - Age 18+ contributes ~3%  

- Demographic updates are adult-driven, with ~90% from age 17+  

- Clear seasonal enrolment peak observed in September 2025  

- High-demand states include:
  - Uttar Pradesh  
  - Bihar  
  - Maharashtra  
  - West Bengal  
  - Madhya Pradesh  

- District- and PIN-level analysis reveals micro-level service hotspots  

- Anomaly detection highlights state-month combinations with sudden enrolment spikes  

- Updates-to-Enrolment Ratio reveals update-heavy regions requiring focused capacity planning  
________________________________________
Datasets Used
1. Aadhaar Enrolment Dataset
•	Daily aggregated enrolment counts at PIN code level
•	Age groups: 0–5, 5–17, 18+
•	Coverage: Mar 2025 – Dec 2025
2. Aadhaar Demographic Update Dataset
•	Daily aggregated demographic update counts at PIN code level
•	Age groups: 5–17, 17+
•	Coverage: Mar 2025 – Dec 2025

Tools & Technologies
•	Python
•	Pandas – data cleaning, aggregation, feature engineering
•	Matplotlib – data visualization
•	Google Colab – exploratory analysis and reporting
________________________________________
## Methodology
-The project methodology begins with the consolidation of multi-part datasets into a unified and structured format to ensure consistency and completeness of information. This is followed by comprehensive data cleaning and preprocessing, including handling missing values, correcting inconsistencies, standardizing formats, and removing duplicates to improve data quality. Feature engineering techniques are then applied, such as calculating aggregate totals and extracting temporal attributes like month and year, to enhance analytical depth. Time-series trend analysis is conducted to identify patterns, seasonality, and growth trends over time. Additionally, geographic analysis at the state, district, and PIN code levels is performed to understand regional variations and distribution patterns. Age-based societal trend analysis is incorporated to examine demographic influences and behavioral differences across age groups. Anomaly detection using month-over-month growth metrics is applied to identify unusual spikes or declines in activity. Key Performance Indicators (KPIs) are designed to enable effective workload comparison and performance measurement across different dimensions. Finally, insights are systematically generated and translated into actionable recommendations using a structured insight generation and recommendation framework to support informed decision-making.
________________________________________
## Analysis Highlights

- Monthly enrolment and update trends  
- Age-wise contribution analysis  
- Top states and districts by service demand  
- PIN code hotspot identification  
- State-month anomaly detection  
- Updates-to-Enrolment Ratio (state-wise KPI)  

## Recommendations

- Seasonal capacity scaling during peak enrolment months  
- Child-focused enrolment workflows  
- District and PIN-level targeted resource deployment  
- Dedicated update service capacity in update-heavy regions  
- KPI-driven dual workload planning  
- Early-warning monitoring using anomaly detection  

## Future Scope

- Real-time analytics dashboard  
- Forecasting models for enrolment and update demand  
- Integration with geospatial visualization tools  
- Automation of anomaly alerts  
________________________________________
## 📂 Project Structure

```
Aadhaar-enrolment-demographic-analysis/
│
├── data/
├── final_graphs_annotated/
├── aadhaar_enrolment_merged.csv
├── aadhaar_demo_merged.csv
├── analysis_notebook.ipynb
└── README.md
```

---

##  Author

Pushkar Gandhi  
UIDAI Hackathon 2026 Participant

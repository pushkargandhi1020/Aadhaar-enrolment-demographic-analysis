# Aadhaar-enrolment-demographic-analysis
Aadhaar Enrolment & Demographic Trends Analysis (India)
Overview
This project presents a comprehensive data-driven analysis of Aadhaar enrolment and demographic update activities across India. Using large-scale aggregated datasets, the analysis uncovers societal trends, geographic hotspots, seasonal patterns, anomalies, and operational KPIs to support better service planning and resource allocation.
The project was developed as part of UIDAI Hackathon 2026 and focuses on transforming raw public data into actionable insights using Python-based analytics.
________________________________________
Objectives
•	Analyze time-based trends in Aadhaar enrolments and demographic updates
•	Identify age-wise societal patterns in enrolment and update behavior
•	Detect state, district, and PIN code hotspots
•	Perform anomaly detection to capture unusual spikes in demand
•	Design a combined KPI (Updates-to-Enrolment Ratio) for workload assessment
•	Propose data-backed recommendations for operational planning
________________________________________
Key Insights
•	Aadhaar enrolment demand is child-driven:
o	Age 0–5 contributes ~65%
o	Age 5–17 contributes ~32%
o	Age 18+ contributes ~3%
•	Demographic updates are adult-driven, with ~90% from age 17+
•	Clear seasonal enrolment peak observed in September 2025
•	High-demand states include Uttar Pradesh, Bihar, Maharashtra, West Bengal, and Madhya Pradesh
•	District- and PIN-level analysis reveals micro-level service hotspots
•	Anomaly detection highlights state-month combinations with sudden enrolment spikes
•	Updates-to-Enrolment Ratio reveals update-heavy regions requiring focused capacity planning
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
🛠️ Tools & Technologies
•	Python
•	Pandas – data cleaning, aggregation, feature engineering
•	Matplotlib – data visualization
•	Google Colab – exploratory analysis and reporting
________________________________________
Methodology
1.	Consolidation of multi-part datasets
2.	Data cleaning and preprocessing
3.	Feature engineering (totals, month extraction)
4.	Time-series trend analysis
5.	Geographic analysis (state, district, PIN code)
6.	Age-based societal trend analysis
7.	Anomaly detection using month-over-month growth
8.	KPI design for workload comparison
9.	Insight generation and recommendation framework
________________________________________
Analysis Highlights
•	Monthly enrolment and update trends
•	Age-wise contribution analysis
•	Top states and districts by service demand
•	PIN code hotspot identification
•	State-month anomaly detection
•	Updates-to-Enrolment Ratio (state-wise KPI)
________________________________________
Recommendations
•	Seasonal capacity scaling during peak enrolment months
•	Child-focused enrolment workflows
•	District and PIN-level targeted resource deployment
•	Dedicated update service capacity in update-heavy regions
•	KPI-driven dual workload planning
•	Early-warning monitoring using anomaly detection
________________________________________
Future Scope
•	Real-time analytics dashboard
•	Forecasting models for enrolment and update demand
•	Integration with geospatial visualization tools
•	Automation of anomaly alerts
________________________________________
Author
Pushkar Gandhi UIDAI Hackathon 2026 Participant


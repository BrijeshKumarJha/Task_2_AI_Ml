# 🏛️ Ancient Temples: Exploratory Data Analysis (EDA)

## 📌 Project Overview
This project is a comprehensive Exploratory Data Analysis (EDA) performed on the `NewAncientTemples.csv` dataset. The primary objective of this task is to understand the dataset using statistical summaries, identify geographic anomalies (outliers), and visualize feature relationships. 

Through this analysis, a critical data entry error was detected and resolved, ensuring the data is clean and ready for any future Machine Learning models.

## 🛠️ Technologies & Libraries Used
* **Python 3.x**
* **Pandas:** Data manipulation, filtering, and summary statistics
* **Matplotlib:** Core plotting framework
* **Seaborn:** Advanced statistical visualizations (`histplot`, `boxplot`, `heatmap`, `pairplot`)

## 🚀 Key EDA Steps & Findings

### 1. Initial Data Inspection & Summary Statistics
Loaded the dataset and utilized `df.info()` and `df.describe()` to understand the distribution of distances from four major Indian metro cities (Mumbai, New Delhi, Chennai, Kolkata). 
* **Initial Discovery:** The maximum distance in the summary statistics showed an impossible value of **7374.45 Km** within India, immediately signaling the presence of an extreme outlier or a data entry error.

### 2. Outlier & Skewness Detection
Visualized the distribution using a Histogram (with KDE) and a Boxplot. The histogram revealed a heavy **Right Skew (Positive Skew)**, and the boxplot clearly isolated the extreme geographic outlier far beyond the normal distribution.

![Histogram and Boxplot](screenshots/Histogram%20and%20Boxplot.png)

### 3. Correlation Analysis
Generated a correlation matrix and visualized it using a Heatmap to understand how distances from different cities move together.
* **Key Finding:** A strong positive correlation (**0.79**) was observed between `DistanceFromMumbai(Km)` and `DistanceFromChennai(Km)`.

![Correlation Heatmap](screenshots/Correlation%20Heatmap.png)

### 4. Anomaly Investigation & Data Cleaning
Using targeted Pandas filtering, the exact row causing the anomaly was isolated:
* **The Culprit:** Row 17 - **Konark Sun Temple, Orissa**
* **The Issue:** The distance from Mumbai was recorded as `6345.52 Km` and from Chennai as `7374.45 Km`. Geographically, India's total width is ~2900 Km, proving this was a severe data entry typographical error. Additionally, its `Location` value was missing (`NaN`).
* **The Fix:** Filtered out rows with impossible distances (`> 6000 Km`), reducing the dataset from 53 to 52 rows and restoring the maximum distance to a logical **~2389 Km**.

![Outlier Detection](screenshots/Outlier%20Detection.png)

### 5. Multi-Variable Relationship Analysis (Pairplot)
After cleaning the dataset, a `pairplot` was generated to inspect the pairwise distributions and scatter relationships across all numeric distance columns simultaneously.

![Pairplot Relationships](screenshots/Pairplot.png)

## 📊 Final Cleaned Data Summary
* **Original Rows:** 53
* **Cleaned Rows:** 52
* **New Max Distance (Mumbai):** `2090.98 Km` (Logically accurate)
* **New Max Distance (Chennai):** `2389.46 Km` (Logically accurate)

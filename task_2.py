import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading dataset...")
df = pd.read_csv('NewAncientTemples.csv')

print("\n--- Data Info ---")
print(df.info())
print("\n" + "="*50 + "\n")

print("--- Summary Statistics ---")
print(df.describe())
print("\n" + "="*50 + "\n")


print("Generating Histogram and Boxplot. Please close the graph window to continue...")
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 5))

# Histogram
plt.subplot(1, 2, 1) 
sns.histplot(df['DistanceFromMumbai(Km)'], kde=True, color='skyblue')
plt.title('Histogram: Distance from Mumbai')

# Boxplot
plt.subplot(1, 2, 2) 
sns.boxplot(x=df['DistanceFromMumbai(Km)'], color='orange')
plt.title('Boxplot: Finding Outliers')

plt.tight_layout()
plt.show() 

print("\nGenerating Correlation Heatmap. Please close the graph window to continue...")
numeric_columns = df[['DistanceFromMumbai(Km)', 'DistanceFromNewDelhi(Km)', 
                      'DistanceFromChennai(Km)', 'DistanceFromKolkata(Km)']]
corr_matrix = numeric_columns.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=1)
plt.title('Correlation Heatmap: Distance Relationships')
plt.show() 


outliers = df[(df['DistanceFromMumbai(Km)'] > 6000) | 
              (df['DistanceFromChennai(Km)'] > 6000)]

print("\n--- 🚨 The REAL Outliers Detected 🚨 ---")
print(outliers[['templeName', 'Location', 'DistanceFromMumbai(Km)', 'DistanceFromChennai(Km)']])
print("\n" + "="*50 + "\n")


df_clean = df[df['DistanceFromMumbai(Km)'] < 6000]

print(f"Original data mein rows: {len(df)}")
print(f"Cleaned data mein rows: {len(df_clean)}")

print("\n--- Summary Statistics (After Cleaning) ---")
print(df_clean[['DistanceFromMumbai(Km)', 'DistanceFromChennai(Km)']].describe().loc[['max']])



print("\nGenerating Pairplot. Please close the graph window to continue...")


sns.pairplot(df_clean[['DistanceFromMumbai(Km)', 'DistanceFromNewDelhi(Km)', 
                       'DistanceFromChennai(Km)', 'DistanceFromKolkata(Km)']], 
             diag_kind='kde', 
             plot_kws={'alpha': 0.6, 'color': 'purple'})


plt.suptitle('Pairplot: Feature Relationships', y=1.02)
plt.show()
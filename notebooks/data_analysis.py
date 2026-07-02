import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

print("loading data...")

# 1. Load the data
df_econ = pd.read_csv('datasets/nigeria_economic_digital_data.csv')
df_sme = pd.read_csv('datasets/nigeria_sme_credit_data.csv')

# 2. Merge the data on 'Year'
df_merged = pd.merge(df_econ, df_sme, on='Year', how='inner')

# 3. Calculate Correlations
# drop Year to just get indicator correlations
corr_matrix = df_merged.drop(columns=['Year']).corr()

print(corr_matrix)

# 4. Generate Correlation Heatmap Figure
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt=".2f")
plt.title("Correlation: Economic Growth, Digital Readiness, and SME Credit in Nigeria")
plt.tight_layout()

# Save the figure
fig_path = 'figures/correlation_heatmap.png'
plt.savefig(fig_path)
print(f"\nSaved correlation heatmap to {fig_path}")

# 5. Extract Key Insights
print("\n--- Key Insights ---")
bb_sme_corr = corr_matrix.loc['broadband_subscriptions', 'Private_Sector_Credit_Pct_GDP']
if bb_sme_corr > 0.5:
    print(f"Strong positive correlation ({bb_sme_corr:.2f}) between broadband adoption and SME credit access.")
elif bb_sme_corr > 0:
    print(f"Moderate positive correlation ({bb_sme_corr:.2f}) between broadband adoption and SME credit access.")
    
bb_gdp_corr = corr_matrix.loc['broadband_subscriptions', 'gdp_growth']
print(f"broadband & gdp correlation: {bb_gdp_corr:.2f}")

# quick write out to a markdown file for the paper draft
with open('paper/analysis_summary.md', 'w') as f:
    f.write("# Quick Analysis Summary\n\n")
    f.write(corr_matrix.to_markdown())
    f.write("\n\n")
    f.write(f"- broadband vs SME credit: {bb_sme_corr:.2f}\n")
    f.write(f"- broadband vs GDP: {bb_gdp_corr:.2f}\n")
print("done writing summary")

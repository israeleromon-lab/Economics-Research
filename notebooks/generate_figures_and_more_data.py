import requests
import pandas as pd
import matplotlib.pyplot as plt
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- 1. Scrape More Data (SME Credit / Private Sector Credit) ---
print("Fetching SME / Private Sector Credit Data...")
BASE_URL = "https://api.worldbank.org/v2/country/NGA/indicator"
# FD.AST.PRVT.GD.ZS = Domestic credit to private sector (% of GDP)
sme_indicator = "FD.AST.PRVT.GD.ZS"

url = f"{BASE_URL}/{sme_indicator}?format=json&per_page=100"
response = requests.get(url, verify=False)
if response.status_code == 200:
    data = response.json()
    if len(data) > 1:
        records = data[1]
        df_sme = pd.DataFrame(records)[['date', 'value']]
        df_sme.columns = ['Year', 'Private_Sector_Credit_Pct_GDP']
        df_sme['Year'] = pd.to_numeric(df_sme['Year'])
        df_sme = df_sme.dropna().sort_values('Year').reset_index(drop=True)
        
        # Filter for recent years 2000+
        df_sme = df_sme[df_sme['Year'] >= 2000]
        
        output_csv = 'datasets/nigeria_sme_credit_data.csv'
        df_sme.to_csv(output_csv, index=False)
        print(f"Saved SME Credit data to {output_csv}")

# --- 2. Generate Figures ---
print("Generating Figures...")
data_path = 'datasets/nigeria_economic_digital_data.csv'
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    
    # We'll plot GDP growth and Broadband over time where data exists
    df_plot = df.dropna(subset=['gdp_growth', 'broadband_subscriptions'])
    
    fig, ax1 = plt.subplots(figsize=(10, 6))

    color = 'tab:red'
    ax1.set_xlabel('Year')
    ax1.set_ylabel('GDP Growth (%)', color=color)
    ax1.plot(df_plot['Year'], df_plot['gdp_growth'], color=color, marker='o', label='GDP Growth')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  
    color = 'tab:blue'
    ax2.set_ylabel('Broadband Subscriptions (%)', color=color)  
    ax2.plot(df_plot['Year'], df_plot['broadband_subscriptions'], color=color, marker='s', label='Broadband')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  
    plt.title("Nigeria GDP Growth vs Digital Readiness (Broadband)")
    
    fig_path = 'figures/gdp_vs_digital_readiness.png'
    plt.savefig(fig_path)
    print(f"Saved figure to {fig_path}")
else:
    print("Economic data not found to generate figure.")

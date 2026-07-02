import requests
import pandas as pd
import os

# Ensure datasets directory exists
os.makedirs('../datasets', exist_ok=True)

print("Fetching World Bank Data for Nigeria...")

# World Bank API base URL
BASE_URL = "https://api.worldbank.org/v2/country/NGA/indicator"

# Indicators
indicators = {
    "gdp_growth": "NY.GDP.MKTP.KD.ZG",
    "financial_inclusion": "FX.OWN.TOTL.ZS",
    "broadband_subscriptions": "IT.NET.BBND.P2" # proxy for digital readiness
}

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_wb_data(indicator_code):
    url = f"{BASE_URL}/{indicator_code}?format=json&per_page=100"
    response = requests.get(url, verify=False)
    
    if response.status_code == 200:
        data = response.json()
        if len(data) > 1:
            records = data[1]
            df = pd.DataFrame(records)
            df = df[['date', 'value']]
            df.columns = ['Year', 'Value']
            df['Year'] = pd.to_numeric(df['Year'])
            df = df.dropna().sort_values('Year').reset_index(drop=True)
            return df
    print(f"Failed to fetch {indicator_code}")
    return pd.DataFrame()

# Fetch and save data
combined_df = pd.DataFrame({'Year': range(2000, 2025)})

for name, code in indicators.items():
    print(f"Fetching {name} ({code})...")
    df = fetch_wb_data(code)
    if not df.empty:
        df = df.rename(columns={'Value': name})
        combined_df = pd.merge(combined_df, df, on='Year', how='left')

# Save to CSV
output_path = '../datasets/nigeria_economic_digital_data.csv'
combined_df.to_csv(output_path, index=False)
print(f"Data saved successfully to {output_path}")

print("\nSample Data:")
print(combined_df.dropna(how='all', subset=list(indicators.keys())).tail(5))

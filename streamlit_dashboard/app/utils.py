import pandas as pd
import os

def load_data():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data'))

    benin = pd.read_csv(os.path.join(base_path, 'benin_clean.csv'))
    sierra = pd.read_csv(os.path.join(base_path, 'sierra_leone_clean.csv'))
    togo = pd.read_csv(os.path.join(base_path, 'togo_clean.csv'))

    # Add a 'Country' column so we can filter
    benin['Country'] = 'Benin'
    sierra['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'

    combined = pd.concat([benin, sierra, togo], ignore_index=True)
    return combined

def get_top_regions(df):
    return df.groupby('Country')['GHI'].mean().sort_values().reset_index().head(5)

import pandas as pd
import numpy as np

def load_and_preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Load and preprocess transaction data."""
    
    # Convert date column
    df['date'] = pd.to_datetime(df['date'])
    
    # Ensure amount is numeric
    df['amount'] = pd.to_numeric(df['amount'])
    
    # Sort by date
    df = df.sort_values('date')
    
    # Create daily aggregation
    daily = df.groupby('date').agg({
        'amount': 'sum'
    }).reset_index()
    
    # Fill missing dates
    date_range = pd.date_range(start=daily['date'].min(), end=daily['date'].max(), freq='D')
    daily = daily.set_index('date').reindex(date_range).fillna(0).reset_index()
    daily.columns = ['date', 'amount']
    
    # Calculate cumulative cash flow
    daily['cumulative'] = daily['amount'].cumsum()
    
    return df

def aggregate_to_monthly(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate daily data to monthly."""
    df['month'] = df['date'].dt.to_period('M')
    monthly = df.groupby('month')['amount'].sum().reset_index()
    monthly['month'] = monthly['month'].dt.to_timestamp()
    return monthly

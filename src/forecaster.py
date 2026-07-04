import pandas as pd
import numpy as np
from prophet import Prophet
import warnings
warnings.filterwarnings('ignore')

class CashFlowForecaster:
    """Time series forecasting using Prophet."""
    
    def __init__(self):
        self.model = None
    
    def forecast(self, df: pd.DataFrame, days: int = 30, confidence: float = 0.85) -> pd.DataFrame:
        """Generate cash flow forecast."""
        
        # Prepare data for Prophet
        daily = df.groupby('date')['amount'].sum().reset_index()
        daily.columns = ['ds', 'y']
        
        # Initialize and fit model
        self.model = Prophet(
            yearly_seasonality=True,
            weekly_seasonality=True,
            daily_seasonality=False,
            interval_width=confidence
        )
        
        self.model.fit(daily)
        
        # Create future dataframe
        future = self.model.make_future_dataframe(periods=days)
        
        # Make predictions
        forecast = self.model.predict(future)
        
        # Filter to future dates only
        future_forecast = forecast[forecast['ds'] > daily['ds'].max()].copy()
        future_forecast = future_forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
        future_forecast.columns = ['date', 'forecast', 'lower_bound', 'upper_bound']
        
        # Calculate cumulative forecast
        future_forecast['cumulative_forecast'] = future_forecast['forecast'].cumsum()
        
        # Add current cash position
        current_cash = daily['y'].sum()
        future_forecast['projected_cash'] = current_cash + future_forecast['cumulative_forecast']
        
        return future_forecast
    
    def get_forecast_summary(self, forecast_df: pd.DataFrame) -> dict:
        """Get summary statistics of forecast."""
        return {
            'total_forecast': forecast_df['forecast'].sum(),
            'avg_daily': forecast_df['forecast'].mean(),
            'min_day': forecast_df.loc[forecast_df['forecast'].idxmin(), 'date'],
            'max_day': forecast_df.loc[forecast_df['forecast'].idxmax(), 'date'],
            'final_cash_position': forecast_df['projected_cash'].iloc[-1]
        }

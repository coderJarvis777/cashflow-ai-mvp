import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_forecast_chart(historical_df: pd.DataFrame, forecast_df: pd.DataFrame):
    """Create interactive forecast chart."""
    
    # Historical data
    daily_hist = historical_df.groupby('date')['amount'].sum().reset_index()
    daily_hist['cumulative'] = daily_hist['amount'].cumsum()
    
    # Create figure
    fig = go.Figure()
    
    # Add historical cumulative
    fig.add_trace(go.Scatter(
        x=daily_hist['date'],
        y=daily_hist['cumulative'],
        mode='lines',
        name='Historical Cash Flow',
        line=dict(color='blue', width=2)
    ))
    
    # Add forecast
    fig.add_trace(go.Scatter(
        x=forecast_df['date'],
        y=forecast_df['projected_cash'],
        mode='lines',
        name='Forecasted Cash Flow',
        line=dict(color='green', width=2, dash='dash')
    ))
    
    # Add confidence interval
    fig.add_trace(go.Scatter(
        x=forecast_df['date'].tolist() + forecast_df['date'].tolist()[::-1],
        y=(forecast_df['projected_cash'] + forecast_df['upper_bound']).tolist() + 
          (forecast_df['projected_cash'] + forecast_df['lower_bound']).tolist()[::-1],
        fill='toself',
        fillcolor='rgba(0, 128, 0, 0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        name='Confidence Interval'
    ))
    
    fig.update_layout(
        title='💰 Cash Flow Forecast',
        xaxis_title='Date',
        yaxis_title='Cash Flow ($)',
        hovermode='x unified',
        height=500
    )
    
    return fig

def create_category_chart(df: pd.DataFrame):
    """Create category breakdown chart."""
    
    # Expense breakdown
    expense_data = df[df['type'] == 'expense'].groupby('category')['amount'].sum().abs().reset_index()
    expense_data.columns = ['category', 'amount']
    expense_data = expense_data.sort_values('amount', ascending=True)
    
    fig = px.bar(
        expense_data,
        x='amount',
        y='category',
        orientation='h',
        title='💸 Expense Breakdown by Category',
        labels={'amount': 'Amount ($)', 'category': 'Category'}
    )
    
    fig.update_layout(height=400)
    
    return fig

import pandas as pd
import numpy as np
from datetime import datetime

class CashFlowAgent:
    """Rule-based financial agent for answering questions."""
    
    def __init__(self, historical_data: pd.DataFrame, forecast_data: pd.DataFrame):
        self.historical = historical_data
        self.forecast = forecast_data
        self._calculate_metrics()
    
    def _calculate_metrics(self):
        """Pre-calculate key metrics."""
        # Historical metrics
        self.total_income = self.historical[self.historical['type'] == 'income']['amount'].sum()
        self.total_expense = abs(self.historical[self.historical['type'] == 'expense']['amount'].sum())
        self.net_cashflow = self.total_income - self.total_expense
        
        # Time period
        days = (self.historical['date'].max() - self.historical['date'].min()).days
        self.months = max(days / 30, 1)
        
        # Monthly averages
        self.avg_monthly_income = self.total_income / self.months
        self.avg_monthly_expense = self.total_expense / self.months
        self.avg_monthly_net = self.net_cashflow / self.months
        
        # Burn rate (monthly expenses)
        self.burn_rate = self.avg_monthly_expense
        
        # Category breakdown
        self.expense_by_category = self.historical[self.historical['type'] == 'expense'].groupby('category')['amount'].sum().abs()
        self.income_by_category = self.historical[self.historical['type'] == 'income'].groupby('category')['amount'].sum()
        
        # Forecast metrics
        self.forecast_days = len(self.forecast)
        self.forecast_total = self.forecast['forecast'].sum()
        self.final_cash = self.forecast['projected_cash'].iloc[-1]
        
        # Cash runway
        current_cash = self.historical['amount'].sum()
        if self.avg_monthly_net < 0:
            self.cash_runway_months = current_cash / abs(self.avg_monthly_net)
        else:
            self.cash_runway_months = float('inf')
    
    def answer(self, question: str) -> str:
        """Answer user questions about cash flow."""
        question = question.lower()
        
        # Burn rate questions
        if 'burn rate' in question or 'monthly expense' in question:
            return f"💸 **Monthly Burn Rate:** ${self.burn_rate:,.2f}\n\nThis is your average monthly expenses. To reduce burn, focus on your top expense categories: {', '.join(self.expense_by_category.nlargest(3).index.tolist())}"
        
        # Cash runway questions
        elif 'run out' in question or 'runway' in question or 'how long' in question:
            if self.cash_runway_months == float('inf'):
                return "✅ **Great news!** Your cash flow is positive. You're not burning cash, so you won't run out at the current rate."
            else:
                return f"⏰ **Cash Runway:** {self.cash_runway_months:.1f} months\n\nAt your current burn rate of ${self.burn_rate:,.2f}/month and net cash flow of ${self.avg_monthly_net:,.2f}/month, you have approximately {self.cash_runway_months:.1f} months of cash remaining."
        
        # Average income questions
        elif 'average income' in question or 'avg income' in question:
            return f"📊 **Average Monthly Income:** ${self.avg_monthly_income:,.2f}\n\nYour top income sources: {', '.join(self.income_by_category.nlargest(3).index.tolist())}"
        
        # Average expense questions
        elif 'average expense' in question or 'avg expense' in question:
            return f"📊 **Average Monthly Expenses:** ${self.avg_monthly_expense:,.2f}\n\nYour top expense categories: {', '.join(self.expense_by_category.nlargest(3).index.tolist())}"
        
        # Seasonal patterns
        elif 'seasonal' in question or 'pattern' in question or 'trend' in question:
            monthly = self.historical.groupby(self.historical['date'].dt.to_period('M'))['amount'].sum()
            trend = "increasing 📈" if monthly.iloc[-1] > monthly.iloc[0] else "decreasing 📉"
            return f"📈 **Trend Analysis:** Your cash flow is {trend}\n\nMonthly net cash flow has gone from ${monthly.iloc[0]:,.2f} to ${monthly.iloc[-1]:,.2f} over {len(monthly)} months."
        
        # Top expenses
        elif 'top expense' in question or 'highest expense' in question or 'biggest expense' in question:
            top_3 = self.expense_by_category.nlargest(3)
            response = "💰 **Top 3 Expense Categories:**\n\n"
            for cat, amount in top_3.items():
                pct = (amount / self.total_expense) * 100
                response += f"- **{cat}**: ${amount:,.2f} ({pct:.1f}%)\n"
            return response
        
        # Top income
        elif 'top income' in question or 'highest income' in question or 'biggest income' in question:
            top_3 = self.income_by_category.nlargest(3)
            response = "💰 **Top 3 Income Sources:**\n\n"
            for cat, amount in top_3.items():
                pct = (amount / self.total_income) * 100
                response += f"- **{cat}**: ${amount:,.2f} ({pct:.1f}%)\n"
            return response
        
        # Forecast questions
        elif 'forecast' in question or 'predict' in question or 'future' in question:
            return f"🔮 **{self.forecast_days}-Day Forecast:**\n\n- Total forecasted cash flow: ${self.forecast_total:,.2f}\n- Projected final cash position: ${self.final_cash:,.2f}\n- Average daily: ${self.forecast['forecast'].mean():,.2f}"
        
        # Net cash flow
        elif 'net' in question or 'profit' in question or 'loss' in question:
            status = "profit ✅" if self.net_cashflow > 0 else "loss ❌"
            return f"📊 **Net Cash Flow:** ${self.net_cashflow:,.2f} ({status})\n\n- Total Income: ${self.total_income:,.2f}\n- Total Expenses: ${self.total_expense:,.2f}\n- Monthly Average: ${self.avg_monthly_net:,.2f}"
        
        # Default response
        else:
            return f"🤔 I can help you with questions about:\n\n- Burn rate and expenses\n- Cash runway and when you'll run out\n- Average income/expenses\n- Seasonal patterns and trends\n- Top expense/income categories\n- Forecasts and predictions\n\nTry asking: 'What's my burn rate?' or 'When will my cash run out?'"

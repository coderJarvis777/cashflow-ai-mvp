# 💰 CashFlow AI - Agentic Cash Flow Forecasting MVP

An AI-powered cash flow forecasting tool that helps small businesses predict their financial future and get intelligent insights through a conversational agent.

## 🚀 Features

- **📊 Data Upload**: Import your transaction data via CSV or Excel
- **🔮 Cash Flow Forecasting**: Generate 30/60/90-day forecasts using Prophet time series model
- **🤖 AI Agent**: Chat with your financial agent to get insights about:
  - Monthly burn rate
  - Cash runway (when you'll run out of money)
  - Average income and expenses
  - Seasonal patterns and trends
  - Top expense and income categories
- **📈 Interactive Visualizations**: Beautiful charts showing historical and forecasted cash flow
- **📥 Export**: Download your forecasts as CSV

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Forecasting**: Prophet (Facebook's time series forecasting library)
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly
- **Agent**: Custom rule-based financial agent

## 📦 Installation

1. **Clone the repository**:
```bash
git clone https://github.com/coderJarvis777/cashflow-ai-mvp.git
cd cashflow-ai-mvp
```

2. **Create a virtual environment** (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## 🎯 Usage

1. **Run the app**:
```bash
streamlit run app.py
```

2. **Open your browser**: Navigate to `http://localhost:8501`

3. **Load data**:
   - Click "Load Sample Data" to try with sample transactions
   - Or upload your own CSV/Excel file

4. **Generate forecast**:
   - Select forecast horizon (30/60/90 days)
   - Adjust confidence level
   - Click "Generate Forecast"

5. **Chat with the agent**:
   - Use quick action buttons or type your own questions
   - Ask about burn rate, cash runway, trends, etc.

## 📋 Data Format

Your CSV/Excel file should have these columns:

| Column | Description | Example |
|--------|-------------|---------|
| `date` | Transaction date (YYYY-MM-DD) | 2026-01-15 |
| `amount` | Transaction amount (negative for expenses) | -1200.00 |
| `category` | Category name | Rent, Sales, Utilities |
| `type` | 'income' or 'expense' | income |
| `description` | Optional description | Office rent January |

## 🎯 Example Questions for the Agent

- "What's my monthly burn rate?"
- "When will my cash run out?"
- "What's my average monthly income?"
- "Show me seasonal patterns"
- "Which category has highest expenses?"
- "What's my net cash flow?"
- "Show me top income sources"

## 🏗️ Project Structure

```
cashflow-ai-mvp/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .env.example          # Environment variables template
├── src/
│   ├── __init__.py
│   ├── data_loader.py    # Data loading and preprocessing
│   ├── forecaster.py     # Prophet forecasting engine
│   ├── agent.py          # Financial AI agent
│   └── visualizer.py     # Chart generation
└── sample_data/
    └── sample_transactions.csv  # Sample data for testing
```

## 🚀 Next Steps & Enhancements

This is an MVP. Here are ideas for v2:

### 🔧 Technical Improvements
- [ ] Add LLM-powered agent (OpenAI/Claude integration)
- [ ] Implement multiple forecasting models (ARIMA, LSTM, Prophet ensemble)
- [ ] Add database integration (PostgreSQL) for persistent storage
- [ ] User authentication and multi-tenant support
- [ ] API endpoints for programmatic access
- [ ] Automated data ingestion from QuickBooks/Xero APIs

### 📊 Feature Additions
- [ ] Anomaly detection for unusual transactions
- [ ] Budget vs. actual tracking
- [ ] Scenario planning (what-if analysis)
- [ ] Multi-currency support
- [ ] Invoice tracking and accounts receivable forecasting
- [ ] Integration with bank feeds (Plaid API)
- [ ] Mobile-responsive bottom navigation
- [ ] Export to PDF reports

### 🤖 AI/ML Enhancements
- [ ] Fine-tune time series foundation models (Lag-Llama, TimeGPT)
- [ ] Add sentiment analysis from financial news
- [ ] Predictive churn analysis
- [ ] Automated financial recommendations
- [ ] Natural language report generation

## 📝 License

MIT License - feel free to use this for your own projects!

## 🤝 Contributing

Contributions welcome! Feel free to open issues or submit pull requests.

## 🙏 Acknowledgments

- Built with inspiration from [TimeCopilot](https://github.com/TimeCopilot/timecopilot)
- Forecasting powered by [Prophet](https://facebook.github.io/prophet/)
- UI framework by [Streamlit](https://streamlit.io/)

---

**Built with ❤️ for small businesses who want to understand their cash flow better.**

import streamlit as st
import pandas as pd
import plotly.express as px
from src.data_loader import load_and_preprocess_data
from src.forecaster import CashFlowForecaster
from src.agent import CashFlowAgent
from src.visualizer import create_forecast_chart, create_category_chart

# Page config
st.set_page_config(page_title="CashFlow AI", page_icon="💰", layout="wide")

# Title
st.title("💰 CashFlow AI - Agentic Cash Flow Forecasting")
st.markdown("Upload your transactions, forecast your future, and chat with your financial AI agent.")

# Sidebar for data upload
st.sidebar.header("📊 Data Input")
uploaded_file = st.sidebar.file_uploader("Upload CSV or Excel file", type=['csv', 'xlsx'])

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = None
if 'forecast' not in st.session_state:
    st.session_state.forecast = None
if 'agent' not in st.session_state:
    st.session_state.agent = None

# Load sample data button
if st.sidebar.button("📥 Load Sample Data"):
    try:
        df = pd.read_csv('sample_data/sample_transactions.csv')
        st.session_state.data = df
        st.sidebar.success("✅ Sample data loaded!")
    except Exception as e:
        st.sidebar.error(f"Error loading sample data: {e}")

# Process uploaded file
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.session_state.data = df
        st.sidebar.success("✅ Data loaded successfully!")
    except Exception as e:
        st.sidebar.error(f"Error loading file: {e}")

# Main content
if st.session_state.data is not None:
    # Data preprocessing
    df = load_and_preprocess_data(st.session_state.data)
    
    # Show data summary
    st.subheader("📈 Data Summary")
    col1, col2, col3, col4 = st.columns(4)
    
    total_income = df[df['type'] == 'income']['amount'].sum()
    total_expense = abs(df[df['type'] == 'expense']['amount'].sum())
    net_cashflow = total_income - total_expense
    avg_monthly = net_cashflow / (df['date'].max() - df['date'].min()).days * 30
    
    col1.metric("Total Income", f"${total_income:,.2f}")
    col2.metric("Total Expenses", f"${total_expense:,.2f}")
    col3.metric("Net Cash Flow", f"${net_cashflow:,.2f}", delta=f"{avg_monthly:,.2f}/mo")
    col4.metric("Transactions", len(df))
    
    # Forecast section
    st.subheader("🔮 Cash Flow Forecast")
    col1, col2 = st.columns([2, 1])
    
    with col2:
        forecast_days = st.selectbox("Forecast Horizon", [30, 60, 90], index=0)
        confidence_level = st.slider("Confidence Level", 0.8, 0.95, 0.85, 0.05)
        
        if st.button("🚀 Generate Forecast", type="primary"):
            with st.spinner("Generating forecast..."):
                forecaster = CashFlowForecaster()
                forecast_df = forecaster.forecast(df, days=forecast_days, confidence=confidence_level)
                st.session_state.forecast = forecast_df
                st.session_state.agent = CashFlowAgent(df, forecast_df)
                st.success("✅ Forecast generated!")
    
    # Display forecast chart
    if st.session_state.forecast is not None:
        fig = create_forecast_chart(df, st.session_state.forecast)
        st.plotly_chart(fig, use_container_width=True)
        
        # Category breakdown
        st.subheader("📊 Category Breakdown")
        fig_cat = create_category_chart(df)
        st.plotly_chart(fig_cat, use_container_width=True)
        
        # Export forecast
        csv = st.session_state.forecast.to_csv(index=False)
        st.download_button(
            label="📥 Download Forecast CSV",
            data=csv,
            file_name="cashflow_forecast.csv",
            mime="text/csv"
        )
    
    # Agent chat section
    if st.session_state.agent is not None:
        st.subheader("🤖 Chat with Your Financial Agent")
        st.markdown("Ask questions about your cash flow, forecasts, and financial insights.")
        
        # Quick action buttons
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("💸 What's my burn rate?"):
                response = st.session_state.agent.answer("What is my monthly burn rate?")
                st.info(response)
        with col2:
            if st.button("⏰ When will cash run out?"):
                response = st.session_state.agent.answer("When will my cash run out?")
                st.info(response)
        with col3:
            if st.button("📊 Average income?"):
                response = st.session_state.agent.answer("What is my average monthly income?")
                st.info(response)
        with col4:
            if st.button("📈 Show trends"):
                response = st.session_state.agent.answer("What are the seasonal patterns?")
                st.info(response)
        
        # Chat input
        user_question = st.text_input("Ask a question:", key="chat_input")
        if user_question:
            with st.spinner("Thinking..."):
                response = st.session_state.agent.answer(user_question)
                st.info(response)
    
    # Raw data viewer
    with st.expander("📋 View Raw Data"):
        st.dataframe(df)

else:
    st.info("👈 Upload a CSV/Excel file or load sample data to get started!")
    
    st.markdown("""
    ### 📋 Expected Data Format
    
    Your CSV should have these columns:
    - **date**: Transaction date (YYYY-MM-DD)
    - **amount**: Transaction amount (negative for expenses)
    - **category**: Category name (e.g., Sales, Rent, Utilities)
    - **type**: 'income' or 'expense'
    - **description**: Optional description
    
    ### 🎯 Example Questions to Ask the Agent
    
    - "What's my monthly burn rate?"
    - "When will my cash run out?"
    - "What's my average monthly income?"
    - "Show me seasonal patterns"
    - "Which category has highest expenses?"
    """)

import streamlit as st
import yfinance as yf
from sklearn.linear_model import LinearRegression
from datetime import date, timedelta
import plotly.graph_objects as go
import ta
class stock_prediction:
                def stock_app():
                    try:
                        st.title("Stock Market Prediction App")
                    
                        # Define the user interface
                        ticker = st.text_input("Enter a stock ticker symbol (e.g. AAPL for Apple):")
                        days = st.slider("Select the number of days for the prediction:", 1, 365, 30)
                        if ticker:
                            st.write(f"Stock prices for {ticker.upper()}:")
                            stock_data = yf.download(ticker, start="2015-01-01", end=date.today())
                            
                            # Add candlestick chart
                            fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                                                 open=stock_data['Open'],
                                                                 high=stock_data['High'],
                                                                 low=stock_data['Low'],
                                                                 close=stock_data['Close'])])
                            fig.update_layout(title=f"{ticker.upper()} Stock Prices", xaxis_title="Date", yaxis_title="Price")
                            st.plotly_chart(fig)
                            st.title("Technical Indicators")
                            # Load the data from Yahoo Finance
                            data = yf.download(ticker, start="2015-01-01", end=date.today())
                            # Calculate the Bollinger Bands
                            indicator_bb = ta.volatility.BollingerBands(close=data['Close'], window=20, window_dev=2)
                            upper_bb = indicator_bb.bollinger_hband()
                            lower_bb = indicator_bb.bollinger_lband()
                            # Calculate the RSI
                            indicator_rsi = ta.momentum.RSIIndicator(close=data['Close'], window=14)
                            rsi = indicator_rsi.rsi()

                            # Calculate the MACD
                            indicator_macd = ta.trend.MACD(close=data['Close'], window_slow=26, window_fast=12, window_sign=9)
                            macd = indicator_macd.macd()
                            signal = indicator_macd.macd_signal()
                            # Create the candlestick chart
                            fig = go.Figure(data=[go.Candlestick(x=data.index,
                                                                 open=data['Open'],
                                                                 high=data['High'],
                                                                 low=data['Low'],
                                                                 close=data['Close'])])
                            # Add the upper and lower Bollinger Bands to the chart
                            fig.add_trace(go.Scatter(x=data.index, y=upper_bb, name='Upper Bollinger Band', line=dict(color='red')))
                            fig.add_trace(go.Scatter(x=data.index, y=lower_bb, name='Lower Bollinger Band', line=dict(color='green')))
                            
                            # Add the RSI to the chart
                            fig.add_trace(go.Scatter(x=data.index, y=rsi, name='RSI', line=dict(color='orange')))
                            
                            # Add the MACD and signal line to the chart
                            fig.add_trace(go.Scatter(x=data.index, y=macd, name='MACD', line=dict(color='blue')))
                            fig.add_trace(go.Scatter(x=data.index, y=signal, name='Signal Line', line=dict(color='purple')))

                            # Add the upper and lower circuit
                            fig.add_trace(go.Scatter(x=data.index, y=[181.39]*len(data.index), name='Upper Circuit', line=dict(color='black', width=1, dash='dash')))
                            fig.add_trace(go.Scatter(x=data.index, y=[148.41]*len(data.index), name='Lower Circuit', line=dict(color='black', width=1, dash='dash')))

                            # Set the title and axis labels
                            fig.update_layout(title=ticker + ' Stock Price', xaxis_title='Date', yaxis_title='Price')

                            # Show the chart
                            st.plotly_chart(fig)

                            X = [[i] for i in range(len(stock_data))]
                            y = stock_data["Close"].values.reshape(-1, 1)
                            model = LinearRegression()
                            model.fit(X, y)
                            last_date = date.today()
                            future_dates = [last_date + timedelta(days=x) for x in range(1, days+1)]
                            future_dates = [d.strftime("%Y-%m-%d") for d in future_dates]
                            future_prices = model.predict([[i] for i in range(len(future_dates))])
                            st.write(f"Predicted stock prices for the next {days} days:")
                            for i in range(len(future_dates)):
                                st.write(future_dates[i], future_prices[i])
                    except:
                            st.warning('Enter correct Symbol')
                                
                            
                            
                            
                            
                            
                            
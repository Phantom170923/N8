import yfinance as yf
import numpy as np


def fetch_stock_data(ticker, start, end, period):
    if period is not None:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)
        return data
    else:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start, end=end)
        return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def rsi_ind(data, periods=14, ema=True):
    '''
    Функция вычисляет RSI индикатор
    '''
    close_delta = data['Close'].diff()
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)

    if ema:
        ma_up = up.ewm(com=int(periods) - 1, adjust=True, min_periods=periods).mean()
        ma_down = down.ewm(com=int(periods) - 1, adjust=True, min_periods=periods).mean()
    else:
        ma_up = up.rolling(window=periods, adjust=False).mean()
        ma_down = down.rolling(window=periods, adjust=False).mean()

    rs = ma_up / ma_down
    rsi = 100 - (100 / (1 + rs))
    return rsi




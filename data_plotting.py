import matplotlib.pyplot as plt
import pandas as pd
import plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot



def create_and_save_plot(data, ticker, start, end, period, style_schedule, filename=None):
    plt.figure(figsize=(10, 6))
    if style_schedule is not None:
        if 'Date' not in data:
            if pd.api.types.is_datetime64_any_dtype(data.index):
                dates = data.index.to_numpy()
                plt.style.use(style_schedule)
                plt.plot(dates, data['Close'].values, label='Close Price')
                plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            else:
                print("Информация о дате отсутствует или не имеет распознаваемого формата.")
                return
        else:
            if not pd.api.types.is_datetime64_any_dtype(data['Date']):
                data['Date'] = pd.to_datetime(data['Date'])
            plt.plot(data['Date'], data['Close'], label='Close Price')
            plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

        plt.title(f"{ticker} Цена акций с течением времени")
        plt.xlabel("Дата")
        plt.ylabel("Цена")
        plt.legend()

        if period is not None:
            if filename is None:
                filename = f"{ticker}_{period}_stock_price_chart_style{style_schedule}.png"
        else:
            if filename is None:
                filename = f"{ticker}_{start}_{end}_stock_price_chart_style{style_schedule}.png"

        plt.savefig(filename)
        print(f"График сохранен как {filename}")
    else:
        return 'Стиль не был введен'


def create_rsi(data, start, end, period, style_schedule, filename=None):
    '''
    Функция cоздает график RSI индикатора
    '''
    if style_schedule is not None:
        plt.figure(figsize=(15, 8))

        dates = data.index.to_numpy()

        plt.plot(dates, data.values)

        plt.xlabel("Дата")
        plt.ylabel("Цена в процентах")
        plt.title('RSI')

        if period is not None:
            if filename is None:
                filename = f"{period}_rsi_create_style{style_schedule}.png"
        else:
            if filename is None:
                filename = f"{start}_{end}rsi_create_style{style_schedule}.png"

        plt.savefig(filename)
        print(f"График сохранен как {filename}")
    else:
        return 'Стиль не был введен'


def create_close_plotly(data):
    '''
    Функция строит интерактивные график цены закрытия
    '''
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            close = go.Scatter(x=dates, y=data['Close'].values, mode='lines', name='Close Price')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        close = go.Scatter(x=data['Date'], y=data['Close'].values, mode='lines', name='Close Price')

    close = [close]
    py.offline.plot(close)

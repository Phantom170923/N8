import data_download as dd
import data_plotting as dplt
import calculate as cl


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс. Также можно ввести период вручную")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца или нажмите Enter, если планируете указать период вручную): ")
    start = input('Введите начало периода для данных (в формате Y-m-d или нажмите Enter, если указали общий период): ')
    end = input('Введите конец периода для данных (в формате Y-m-d или нажмите Enter, если указали общий период): ')

    style = ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid','bmh', 'classic',
             'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright',
             'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid',
             'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper',
             'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks',
             'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']

    style_schedule = input(f'Введите стиль для графика: {style}): ')

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, start, end, period)
    print(stock_data)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, start, end, period, style_schedule)

    # Расчет RSI индикатора
    my_data = dd.rsi_ind(stock_data, periods=14)

    # График RSI индикатора
    dplt.create_rsi(my_data, start, end, period, style_schedule)

    # Интерактивный график цены закрытия
    dplt.create_close_plotly(stock_data)

    # Average value the data
    print(cl.calculate_and_display_average_price(data=stock_data))

    # Вывод максимального и минимального значения цены закрытия и сравнивает разницу с заданным порогом
    print(cl.notify_if_strong_fluctuations(stock_data, 5))

    # Вывод стандатного отклонения цены закрытия
    print(cl.std_ind(stock_data))

    # Экспорт csv файла
    cl.export_data_to_csv(stock_data, input('Введите название для csv файла -> '))


if __name__ == "__main__":
    main()

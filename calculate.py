import pandas as pd
import csv
import numpy as np


def calculate_and_display_average_price(data):
    '''
    Функция вычисляет cредняя ценa акций колонки 'Close' за указанный период
    '''

    average = round(sum(data['Close'] / len(data['Close'])), 2)
    return f'Средняя ценa акций за указанный период: {str(average)}p.'


def notify_if_strong_fluctuations(data, threshold):
    '''
    Функция вычисляет максимальное и минимальное значения цены закрытия и сравнивать разницу с заданным порогом
    '''

    change = int((max(data['Close']) - min(data['Close'])) / min(data['Close']) * 100)

    if change > threshold:
        return f'Процентное изменение превышает заданный порог: Процентное изменение -> {change}, заданный попрог -> {threshold}'
    elif change < threshold:
        return f'Процентное изменение ниже, чем заданный порог: Процентное изменение -> {change}, заданный попрог -> {threshold}'
    else:
        return 'Процентное изменение и заданный порог равны'


def export_data_to_csv(data, filename):
    '''
    Функция экспортирует данные в csv файл
    '''
    try:
        data.to_csv(filename, index=False)
    except Exception as exc:
        return f'Возникла ошибка при сохранении в файл {exc}'


def std_ind(data):
    '''
    Функция вычисляет стандартное отклонение цены закрытия
    '''

    std = np.std(data['Close'])

    return f'Cтандартное отклонение цены закрытия = {std}'

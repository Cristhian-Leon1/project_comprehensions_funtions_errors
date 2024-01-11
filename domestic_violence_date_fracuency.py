import read
import chart


def split_dates(fechas_str):
    try:
        dia, mes, anio = map(int, fechas_str.split('/'))
        return dia, mes, anio
    except ValueError:
        return None


def months_frequency(data_csv):
    new_data = data_csv.copy()
    dates = list(map(lambda x: x['FECHA HECHO'], new_data))
    quantities = list(map(lambda x: x['CANTIDAD'], new_data))

    filtered_data = [(date, quantity) for date, quantity in zip(dates, quantities) if split_dates(date) is not None]
    dates_filtered, quantities_filtered = zip(*filtered_data)
    day, month, year = zip(*map(split_dates, dates_filtered))

    month_unique = list(set(month))
    sum_by_month = {month: 0 for month in month_unique}
    data_dict = zip(month, quantities_filtered)
    for month, quantity in data_dict:
        sum_by_month[month] += int(quantity)

    labels_x = list(sum_by_month.keys())
    values_y = list(sum_by_month.values())

    return labels_x, values_y


if __name__ == '__main__':
    data = read.read_csv('./data.csv')
    labels, values = months_frequency(data)
    chart.generate_bar_chart(labels, values)

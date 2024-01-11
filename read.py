import csv


def read_csv(path):
    with open(path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        header = next(reader)
        data_csv = []
        for row in reader:
            iterable = zip(header, row)
            violence_dict = {key: value for key, value in iterable}
            data_csv.append(violence_dict)
    return data_csv

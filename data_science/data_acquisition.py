import csv


def read_csv(csv_file_path):

    data = {}

    with open(csv_file_path) as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:

            for key, value in row.items():
                if key in data:
                    data[key].append(value)
                else:
                    data[key] = [value]

    return data
import csv
# opening csv files
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)

    csv_file.seek(0)

    for line in csv_reader:
        print(line[2])

    csv_file.seek(0)

    next(csv_reader)
    for line in csv_reader:
        print(line[1])

# copying one file to another
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_csv_file.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)

# parsing
with open('new_csv_file.csv', 'r') as f1:
    csv_reader = csv.reader(f1, delimiter='\t')

    for line in csv_reader:
        print(line)

# dictionary reader and writer

with open('names.csv', 'r') as f2:
    csv_reader = csv.DictReader(f2)

    for line in csv_reader:
        print(line)

    f2.seek(0)

    for line in csv_reader:
        print(line['email'])

with open('names.csv', 'r') as f3:
    csv_reader = csv.DictReader(f3)

    with open('new_csv02.csv', 'w') as f4:
        fieldnames = ['first_name', 'last_name', 'email']
        # fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(f4, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            # del line['email']
            csv_writer.writerow(line)
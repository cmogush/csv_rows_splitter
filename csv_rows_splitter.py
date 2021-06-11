import csv
sourceFolder = r"C:\Users\Chris\Desktop\Python Scripts\csv_rows_splitter\Source CSVs"
resultFolder = r"C:\Users\Chris\Desktop\Python Scripts\csv_rows_splitter\Result"
csv_name = "EDCB.csv"
csv_in = sourceFolder+"\\"+csv_name

"""Read in CSV"""
with open(csv_in) as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        new_csv_name = "{}_{}.csv".format(row['School'], row['CourseCode'])
        csv_out = resultFolder+"\\"+new_csv_name
        with open(csv_out, 'w', newline='') as csv_file_out:
            keys = dict.fromkeys(row)
            writer = csv.DictWriter(csv_file_out, fieldnames=keys)
            writer.writeheader()
            writer.writerow(row)
import csv

sourceFolder = r"C:\Users\Chris\Desktop\Python Scripts\csv_rows_splitter\Source CSVs"
resultFolder = r"C:\Users\Chris\Desktop\Python Scripts\csv_rows_splitter\Result"
csv_name = "0 QA School ESW"
csv_in = sourceFolder + "\\" + csv_name + ".csv"

"""Main"""
with open(csv_in) as csv_file:  # open csv
    reader = csv.DictReader(csv_file)  # read in csv to DictReader
    for row in reader:  # iterate over all rows in reader (csv)
        new_csv_name = "{}_{}".format(row['School'], row['CourseCode'])  # get new csv name from cols
        csv_out = resultFolder + "\\" + new_csv_name + ".csv"  # set csv out location
        with open(csv_out, 'w', newline='') as csv_file_out:  # open output csv
            keys = dict.fromkeys(row)  # set headers from row to keys
            writer = csv.DictWriter(csv_file_out, fieldnames=keys)  # set the keys as headers for new csv
            writer.writeheader()  # write header row to new csv
            writer.writerow(row)  # write the row to new csv

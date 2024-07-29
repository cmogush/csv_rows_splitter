import csv

sourceFolder = r"C:\Users\Chris\Desktop\Python Scripts\csv_rows_splitter\Source CSVs"
resultFolder = r"C:\Users\Chris\Desktop\Python Scripts\csv_rows_splitter\Result"
csv_rename_list = "Genius_Institution_list"  #contains list of new names
csv_template = "ISS_Genius_Import_Template"
csv_in = sourceFolder + "\\" + csv_template + ".csv"
csv_list = sourceFolder + "\\" + csv_rename_list + ".csv"

"""Main"""
with open(csv_list) as csv_renamer_file : #open renamer csv
    reader_renamer = csv.DictReader(csv_renamer_file)  #read in csv to DictReader
    for row_renamer in reader_renamer:
        new_name = row_renamer['SchoolName']
        new_csv_name = "{}".format(new_name)  # get new csv name from cols
        csv_out = resultFolder + "\\" + new_csv_name + ".csv"  # set csv out location

        with open(csv_out, 'w', newline='') as csv_file_out:  # open output csv
            keys = ['Section Code', 'Organization Name', 'School Term', 'Genius School Term']
            writer = csv.DictWriter(csv_file_out, fieldnames=keys)  # set the keys as headers for new csv
            writer.writeheader()  # write header row to new csv

            with open(csv_in) as csv_file:  # open csv
                reader_template = csv.DictReader(csv_file)  # read in csv to DictReader
                for row in reader_template:
                    row['Organization Name'] = new_name
                    writer.writerow(row)  # write the row to new csv
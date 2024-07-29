import pandas as pd
import os

# Specify the input and output directories
input_dir = r'C:\Users\Chris\Desktop\Python Scripts\csv_rows_splitter\Result'
output_dir = r'C:\Users\Chris\Desktop\Python Scripts\csv_rows_splitter\XLS'

# Get a list of all CSV files in the input directory
csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

# Iterate through each CSV file
for csv_file in csv_files:
    # Construct the full input and output file paths
    input_path = os.path.join(input_dir, csv_file)
    output_path = os.path.join(output_dir, csv_file.replace('.csv', '.xls'))

    # Read the CSV file into a pandas dataframe
    df = pd.read_csv(input_path)

    # Write the dataframe to an XLS file
    df.to_excel(output_path, index=False)

    print(f'Converted {csv_file} to {output_path}')
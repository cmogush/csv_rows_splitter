# CSV Row Splitter Toolkit

Takes a CSV and creates generates new CSVs for each row in the CSV

**Course Sync CSV Generator | Single Row to Single File Exporter**

**Filename:** `csv_rows_splitter.py`

### Purpose  
Creates a separate CSV file for each row in a source CSV, naming the output file based on the `School` and `CourseCode` columns. Useful for pushing courses from Pub to Sub

### How It Works
- Reads a CSV, e.g. `0 QA School ESW.csv`.
- For every row:
  - Creates a new file named `{School}_{CourseCode}.csv`.
  - Writes the single row (with headers) to that file.

### Output
- Individual CSVs for each row
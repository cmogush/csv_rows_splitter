# CSV Row Splitter Toolkit

This toolkit contains three Python scripts designed to automate the splitting, renaming, and format conversion of CSV data for easier manipulation, review, or import into external systems (e.g., Genius SIS). The process takes source data, generates customized files, and optionally converts them to Excel format.

---

## Script 1 – **Section Push CSV Generator | Institution-Specific CSV Generator**

**Filename:** `csv_renamer.py`

### Purpose
To Generate the CSVs for pushing sections to Genius
Generates a separate CSV file for each institution listed in a reference file, using a shared course section template.

### How It Works
- Reads a list of institution names from `Genius_Institution_list.csv`.
- For each school:
  - Duplicates all rows from `ISS_Genius_Import_Template.csv`.
  - Replaces the `Organization Name` column with the school's name.
  - Writes the updated rows to a new file named after the school.

### Output
- One CSV file per institution is saved in the `Result` folder.
- Output files include these columns:
  - `Section Code`
  - `Organization Name`
  - `School Term`
  - `Genius School Term`

---

## Script 2 – **Course Sync CSV Generator | Single Row to Single File Exporter**

**Filename:** `csv_rows_splitter.py`

### Purpose  
Creates a separate CSV file for each row in a source CSV, naming the output file based on the `School` and `CourseCode` columns.

### How It Works
- Reads `0 QA School ESW.csv`.
- For every row:
  - Creates a new file named `{School}_{CourseCode}.csv`.
  - Writes the single row (with headers) to that file.

### Output
- Individual CSVs for each row, useful for reviewing or importing isolated course entries.

---

## Script 3 – **CSV to Excel Converter**

**Filename:** `csv_to_xls.py`

### Purpose  
Converts all `.csv` files in the `Result` directory to `.xls` format using `pandas`.

### How It Works
- Scans the `Result` folder for `.csv` files.
- Converts each to `.xls` and saves it in the `XLS` folder.
- File contents and structure are preserved.

### Output
- One `.xls` file per input CSV in the `XLS` folder.
- File names match the original CSV names (with `.xls` extension).

---

## Folder Structure


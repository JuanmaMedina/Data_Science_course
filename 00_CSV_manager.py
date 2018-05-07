"""
Reading and writing CSV files using lists
"""
 
import csv
import os
 
 
# Establish working directory
os.chdir("/home/bioinfor1/Downloads")
 
def print_table(table):
    """
    Echo a nested list to the console
    """
    for row in table:
        print(row)
 
 
def read_csv_file(file_name, file_delimiter):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Lists of lists consisting of the fields in the CSV file
    """
 
    my_table = []
 
    # If csvfile is a file object, it should be opened with newline='' (see footnote for more details)
    with open(file_name, mode='r', newline='') as csvfile:   # don't need to explicitly close the file now
        reader = csv.reader(csvfile, delimiter=file_delimiter, skipinitialspace=True)
 
        for row in reader:
            my_table.append(row)
 
    return my_table
 
 
 
def write_csv_file(csv_table_out, file_name_in, file_delimiter, quoting_value):
    """
    Input: Nested list csv_table and a string file_name
    Action: Write fields in csv_table into a comma-separated CSV file with the name file_name
    """
 
    with open(file_name_in, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=file_delimiter, quoting=quoting_value)
 
        for row in csv_table_out:
            writer.writerow(row)
 
 
def test_part1_code():
    """
    Run examples that test the functions for part 1
    """
 
    # Simple test for reader
    test_table = read_csv_file("test_case.csv", ',')  # create a small CSV for this test
    print_table(test_table)
    print()
 
    # Test the writer
    cancer_risk_table = read_csv_file("cancer_risk05_v4_county.csv", ',')
    write_csv_file(cancer_risk_table, "cancer_risk05_v4_county_copy.csv", ',', csv.QUOTE_MINIMAL)
    cancer_risk_copy = read_csv_file("cancer_risk05_v4_county_copy.csv", ',')
 
    # Test whether two tables are the same
    for row in range(len(cancer_risk_table)):
        for col in range(len(cancer_risk_table[0])):
            if cancer_risk_table[row][col] != cancer_risk_copy[row][col]:
                print("Difference at", row, col, cancer_risk_table[row][col], cancer_risk_copy[row][col])
 
test_part1_code()
 
 
"""
If newline='' is not specified, newlines embedded inside quoted fields will not be interpreted correctly,
and on platforms that use \r\n line endings on write an extra \r will be added.
It should always be safe to specify newline=''
"""

"Processing tabular data through the CSV module, Python Data Analysis course, Rice University"

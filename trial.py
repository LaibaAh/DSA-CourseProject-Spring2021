import csv_to_sqlite 

options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250") 
input_files = ["inventory - Sheet1.csv"] # pass in a list of CSV files
csv_to_sqlite.write_csv(input_files, "output.sqlite", options) #[1]



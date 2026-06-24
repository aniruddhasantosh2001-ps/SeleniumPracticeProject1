import openpyxl

# File ---> Workbook ---> Sheets ---> Rows ---> Cells

file=(r"C:\Users\santo\Downloads\May.xlsx")
workbook=openpyxl.load_workbook(file)
sheet=workbook["Sheet20"]

for r in range(1,6):
    for c in range (1,4):
        sheet.cell(r,c).value="welcome"

workbook.save(file)
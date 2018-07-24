import xlrd
workbook=xlrd.open_workbook("name.xlsx")
worksheet=workbook.sheet_by_index(0)
print("the value of row and coluim 2 is:{0}".format(worksheet.cell(4,2).value))
total_rows=worksheet.nrows
total_cols=worksheet.ncols
print("number of rows= {0},and nombre of colonnnes : {1}".format(total_rows,total_cols))
table=list()
record=list()


for x in range(total_rows):
     for y in range(total_cols):
         record.append(worksheet.cell(x,y).value)
     table.append(record)
     record=[]
     x+=1
print(table)


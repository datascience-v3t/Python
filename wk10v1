import openpyxl
wb = openpyxl.load_workbook('realestatedata.xlsx')
mysheets = wb.sheetnames

print("print all sheets in Excel Workbook")
for x in mysheets:
  print(x)

realestatedata = wb['stouffville']

print("print type sheet")
print(type(realestatedata))
print("sheet name") 
print(realestatedata.title)

print("Value of A1")
data1 = realestatedata['A1']
print(data1.value)

print("goal = get the average of all selling prices");
for i in range(1, 190):
	price = realestatedata.cell(row=i, column=4).value;
	print(price);
	houseType = realestatedata.cell(row=i, column=1).value;
	print(houseType);
	description = realestatedata.cell(row=i, column=2).value;
	print(description);
	numberBedrooms = realestatedata.cell(row=i, column=3).value;
	print(numberBedrooms);

	#type, description, number of bedrooms, price
	#houseprice = ()

# next goal = deposit this data into a data structure

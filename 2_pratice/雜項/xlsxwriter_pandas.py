print()
import pandas as pd

#Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

#Create a Pandas dataframe from the data.
df = pd.DataFrame({'Data':[10,20,30,20,15,30,45]})
print(df)

#Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

#Get the xlsxwriter objects from the dataframe writer object.
workbook = writer.book
worksheet = writer.sheets['Sheet1']
#Apply a conditional format to the cell range.
worksheet.conditional_format('B2:B8', {'type': '3_color_scale'})

#Create a chart object.
chart = workbook.add_chart({'type': 'column'})

#Configure the series of the chart from the dataframe data.
chart.add_series({'values': '=Sheet1!$B$2:$B$8'})

#Insert the chart into the worksheet.
worksheet.insert_chart('C2', chart)

#Close the Pandas Excel writer and outpur the Excel file.
writer.save()

print()